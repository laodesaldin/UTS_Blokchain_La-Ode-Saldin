"""
LEVEL 9 — Mining Reward, Saldo, dan Validasi Ekonomi (LATIHAN)
====================================================================

Inilah langkah menuju cryptocurrency sederhana:
  * Penambang mendapat hadiah (coinbase transaction) dari "sistem" (sender = "0").
  * Saldo setiap alamat dihitung dari SELURUH riwayat transaksi (model akun).
  * Transaksi ditolak jika saldo pengirim tidak cukup (mencegah double spending
    sederhana di dalam mempool).

Tujuan belajar:
  * Asal-usul koin baru (coinbase) dan total suplai.
  * Validasi ekonomi selain validasi kriptografis.

Jalankan tes:  python cek_nilai.py 9
"""

import hashlib
import json

SISTEM = "0"          # pengirim khusus untuk hadiah mining
MINING_REWARD = 10


class Blockchain:
    # ====================== SUDAH DISEDIAKAN ======================
    def __init__(self, difficulty: int = 2):
        self.difficulty = difficulty
        self.pending_transactions = []
        genesis = {"index": 0, "transactions": [], "previous_hash": "0" * 64, "nonce": 0}
        self._tambang(genesis)
        self.chain = [genesis]

    @staticmethod
    def hash_block(block):
        isi = {k: v for k, v in block.items() if k != "hash"}
        return hashlib.sha256(json.dumps(isi, sort_keys=True).encode()).hexdigest()

    def _tambang(self, block):
        block["nonce"] = 0
        while not self.hash_block(block).startswith("0" * self.difficulty):
            block["nonce"] += 1
        block["hash"] = self.hash_block(block)
        return block

    # ============ BAGIAN YANG DIKERJAKAN (isi semua TODO) ============
    def saldo(self, alamat: str, termasuk_pending: bool = True) -> float:
        """Saldo = total diterima - total dikirim, dari semua transaksi di chain.
        Jika termasuk_pending=True, transaksi di pending_transactions ikut dihitung.
        """
        semua_tx = [tx for block in self.chain for tx in block["transactions"]]
        if termasuk_pending:
            semua_tx = semua_tx + list(self.pending_transactions)
        total = 0
        for tx in semua_tx:
            if tx["recipient"] == alamat:
                total += tx["amount"]
            if tx["sender"] == alamat:
                total -= tx["amount"]
        return total

    def add_transaction(self, sender: str, recipient: str, amount) -> None:
        """Tambahkan transaksi ke pending_transactions. Lempar ValueError jika:
          * sender == SISTEM (hanya mine() yang boleh membuat koin)
          * amount <= 0
          * saldo(sender, termasuk_pending=True) < amount
        """
        if sender == SISTEM:
            raise ValueError("Hanya mine() yang boleh membuat koin dari SISTEM")
        if amount <= 0:
            raise ValueError("Amount harus positif")
        if self.saldo(sender, termasuk_pending=True) < amount:
            raise ValueError("Saldo pengirim tidak mencukupi")
        self.pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
        })

    def mine(self, alamat_penambang: str) -> dict:
        """Buat blok baru yang berisi:
          1. Transaksi coinbase {'sender': SISTEM, 'recipient': alamat_penambang,
             'amount': MINING_REWARD} di POSISI PERTAMA
          2. diikuti semua pending_transactions
        Tambang dengan self._tambang, tambahkan ke chain, kosongkan pending.
        Format blok: {index, transactions, previous_hash, nonce}.
        """
        last = self.chain[-1]
        coinbase = {"sender": SISTEM, "recipient": alamat_penambang, "amount": MINING_REWARD}
        block = {
            "index": last["index"] + 1,
            "transactions": [coinbase] + list(self.pending_transactions),
            "previous_hash": last["hash"],
            "nonce": 0,
        }
        self._tambang(block)
        self.chain.append(block)
        self.pending_transactions = []
        return block

    def total_suplai(self) -> float:
        """Jumlah semua koin yang pernah dibuat (jumlah amount transaksi dari SISTEM di chain)."""
        return sum(
            tx["amount"]
            for block in self.chain
            for tx in block["transactions"]
            if tx["sender"] == SISTEM
        )

    def validasi_ekonomi(self) -> bool:
        """True jika, untuk setiap blok selain genesis:
          * transaksi pertama adalah coinbase (sender SISTEM) dengan amount == MINING_REWARD
          * tidak ada transaksi lain dari SISTEM di blok itu
        DAN jika semua transaksi diputar ulang berurutan dari awal, tidak ada
        alamat (selain SISTEM) yang saldonya pernah negatif.
        """
        buku_saldo = {}
        for block in self.chain[1:]:
            txs = block.get("transactions", [])
            if not txs:
                return False
            cb = txs[0]
            if cb.get("sender") != SISTEM or cb.get("amount") != MINING_REWARD:
                return False
            buku_saldo[cb["recipient"]] = buku_saldo.get(cb["recipient"], 0) + cb["amount"]
            for tx in txs[1:]:
                if tx.get("sender") == SISTEM:
                    return False
                pengirim = tx["sender"]
                penerima = tx["recipient"]
                jumlah = tx["amount"]
                if jumlah <= 0 or buku_saldo.get(pengirim, 0) < jumlah:
                    return False
                buku_saldo[pengirim] = buku_saldo.get(pengirim, 0) - jumlah
                buku_saldo[penerima] = buku_saldo.get(penerima, 0) + jumlah
        return True


if __name__ == "__main__":
    bc = Blockchain()
    bc.mine("ani")                       # Ani dapat 10
    bc.add_transaction("ani", "budi", 4)
    bc.mine("citra")                     # Citra dapat 10
    for nama in ("ani", "budi", "citra"):
        print(f"Saldo {nama}: {bc.saldo(nama)}")
    print("Total suplai:", bc.total_suplai())
    try:
        bc.add_transaction("budi", "dodi", 100)
    except ValueError as e:
        print("Ditolak:", e)
    print("Validasi ekonomi:", bc.validasi_ekonomi())
