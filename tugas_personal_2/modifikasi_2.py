"""
TUGAS PERSONAL 2 — Modifikasi Level 6–9 (DIKERJAKAN MAHASISWA)
========================================================

Setiap modifikasi mengubah kode level sebelumnya agar memakai data pribadi
mahasiswa dan menghasilkan angka yang BISA DIHITUNG ULANG (deterministik).

Jalankan:  python tugas_personal_2/jalankan_tugas_2.py
"""

import hashlib

from ecdsa import SECP256k1, SigningKey

import level06_difficulty as L6
import level07_tanda_tangan as L7
import level08_jaringan as L8
import level09_reward_saldo as L9


# ============================================================== MODIFIKASI 6
def jejak_difficulty(awal: int, daftar_waktu: list, target: float) -> list:
    """Terapkan L6.sesuaikan_difficulty berulang kali.

    Mulai dari difficulty `awal`. Untuk setiap waktu di `daftar_waktu` (berurutan),
    hitung difficulty baru dari difficulty saat ini. Kembalikan list semua
    difficulty SETELAH setiap langkah (panjangnya = len(daftar_waktu)).

    Contoh: jejak_difficulty(4, [1, 5, 30], 10) -> [5, 5, 4]
    """
    hasil = []
    sekarang = awal
    for w in daftar_waktu:
        sekarang = L6.sesuaikan_difficulty(sekarang, w, target)
        hasil.append(sekarang)
    return hasil


# ============================================================== MODIFIKASI 7
def kunci_dari_data(nama: str, nim4: str, tanggal_lahir: str):
    """Buat pasangan kunci SECP256k1 yang SELALU SAMA untuk data yang sama.

    secret = int(SHA-256(f"{nim4}:{nama}:{tanggal_lahir}"), 16) % SECP256k1.order
    (jika hasilnya 0, pakai 1). Lalu SigningKey.from_secret_exponent(secret, curve=SECP256k1).
    Kembalikan (kunci_privat_hex, kunci_publik_hex), format sama seperti Level 7.

    PERINGATAN: ini hanya untuk latihan. Kunci asli TIDAK BOLEH dibuat dari data
    yang bisa ditebak orang lain.
    """
    teks = f"{nim4}:{nama}:{tanggal_lahir}"
    secret = int(hashlib.sha256(teks.encode("utf-8")).hexdigest(), 16) % SECP256k1.order
    if secret == 0:
        secret = 1
    sk = SigningKey.from_secret_exponent(secret, curve=SECP256k1)
    vk = sk.get_verifying_key()
    return sk.to_string().hex(), vk.to_string().hex()


def tanda_tangani_deterministik(tx: dict, kunci_privat_hex: str) -> str:
    """Seperti L7.tanda_tangani, tetapi memakai sign_deterministic (RFC 6979),
    sehingga transaksi dan kunci yang sama SELALU menghasilkan tanda tangan yang sama.
    Pesan yang ditandatangani: L7.pesan_transaksi(tx).
    """
    sk = SigningKey.from_string(bytes.fromhex(kunci_privat_hex), curve=SECP256k1)
    return sk.sign_deterministic(L7.pesan_transaksi(tx)).hex()


# ============================================================== MODIFIKASI 8
class NodePersonal(L8.Node):
    """Node Level 8 yang menandai setiap blok tambangannya.

    tambang_blok(transactions) menambang blok dengan daftar transaksi
    [f"{self.nama}#{self.nim4}"] + transactions  (penanda di posisi pertama).
    Gunakan tambang_blok milik kelas induk (super()).
    """

    def __init__(self, nama: str, nim4: str, difficulty: int = 2):
        super().__init__(nama, difficulty)
        self.nim4 = nim4

    def tambang_blok(self, transactions) -> dict:
        return super().tambang_blok([f"{self.nama}#{self.nim4}"] + list(transactions))


def semua_sepakat(nodes: list) -> bool:
    """True jika rantai semua node sama persis."""
    if not nodes:
        return True
    acuan = nodes[0].chain
    return all(n.chain == acuan for n in nodes)


# ============================================================== MODIFIKASI 9
class BlockchainHalving(L9.Blockchain):
    """Blockchain Level 9 dengan hadiah mining yang berkurang separuh (halving),
    seperti Bitcoin.

    hadiah(index) = hadiah_awal // 2 ** ((index - 1) // interval)
      contoh hadiah_awal=40, interval=2: blok 1-2 = 40, blok 3-4 = 20, blok 5-6 = 10, ...

    Ubah mine() dan validasi_ekonomi() dari Level 9 agar memakai hadiah(index)
    sebagai pengganti konstanta MINING_REWARD.
    """

    def __init__(self, hadiah_awal: int, interval: int, difficulty: int = 2):
        super().__init__(difficulty)
        self.hadiah_awal = hadiah_awal
        self.interval = interval

    def hadiah(self, index: int) -> int:
        return self.hadiah_awal // (2 ** ((index - 1) // self.interval))

    def mine(self, alamat_penambang: str) -> dict:
        last = self.chain[-1]
        idx = last["index"] + 1
        coinbase = {"sender": L9.SISTEM, "recipient": alamat_penambang, "amount": self.hadiah(idx)}
        block = {
            "index": idx,
            "transactions": [coinbase] + list(self.pending_transactions),
            "previous_hash": last["hash"],
            "nonce": 0,
        }
        self._tambang(block)
        self.chain.append(block)
        self.pending_transactions = []
        return block

    def validasi_ekonomi(self) -> bool:
        buku_saldo = {}
        for block in self.chain[1:]:
            txs = block.get("transactions", [])
            if not txs:
                return False
            cb = txs[0]
            if cb.get("sender") != L9.SISTEM or cb.get("amount") != self.hadiah(block["index"]):
                return False
            buku_saldo[cb["recipient"]] = buku_saldo.get(cb["recipient"], 0) + cb["amount"]
            for tx in txs[1:]:
                if tx.get("sender") == L9.SISTEM:
                    return False
                pengirim = tx["sender"]
                penerima = tx["recipient"]
                jumlah = tx["amount"]
                if jumlah <= 0 or buku_saldo.get(pengirim, 0) < jumlah:
                    return False
                buku_saldo[pengirim] = buku_saldo.get(pengirim, 0) - jumlah
                buku_saldo[penerima] = buku_saldo.get(penerima, 0) + jumlah
        return True
