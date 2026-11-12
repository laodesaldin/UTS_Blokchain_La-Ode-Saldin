# Tugas Blockchain — Midtest (Level 1 — Level 9)

- **Nama:** La Ode Saldin
- **NIM:** 202355202067 (`2067`)
- **Mata Kuliah:** Teknologi Blockchain

Implementasi teknologi Blockchain dari nol menggunakan Python (Level 1 sampai Level 9) beserta Tugas Personal dan Laporan Analisis.

---

## Struktur Berkas Proyek

### Materi 1 – 5
1. **`level01_hash.py`** — Fungsi Hash SHA-256 (`sha256_hex`), serialisasi kanonik (`hash_dict`), dan demonstrasi *Avalanche Effect* (`bit_berbeda`, `persen_bit_berbeda`).
2. **`level02_blok.py`** — Struktur blok dasar, penambangan Proof of Work (`mine_block`), dan validasi rantai (`chain_valid`).
3. **`level03_tampering.py`** — Eksperimen manipulasi data (`ubah_blok`), deteksi tautan putus (`cari_tautan_putus`), dan penyambungan ulang (`sambung_ulang`).
4. **`level04_transaksi.py`** — Mempool (`pending_transactions`), validasi transaksi (`add_transaction`), dan pelacakan riwayat transaksi (`riwayat`).
5. **`level05_pow_nonce.py`** — Proof of Work berbasis `nonce` atas seluruh isi blok dan eksperimen penambangan ulang (`tambang_ulang_dari`).
6. **`tugas_personal/`** — Modifikasi Level 1–5 menggunakan data pribadi mahasiswa (`data_saya.py`, `modifikasi.py`, `skenario.py`, `jalankan_tugas.py`).
- **Laporan Analisis Materi 1–5:**
  - [`laporan_tugas_personal_Materi 1 -5.md`](./laporan_tugas_personal_Materi%201%20-5.md)
  - [`tugas_personal/laporan_tugas_personal_2067.md`](./tugas_personal/laporan_tugas_personal_2067.md)

### Materi 6 – 9 & Tugas Personal 2
7. **`level06_difficulty.py`** — Eksperimen tingkat kesulitan (*difficulty*), ekspektasi matematis $16^d$, dan penyesuaian *difficulty* (`sesuaikan_difficulty`).
8. **`level07_tanda_tangan.py`** — Pasangan kunci kriptografi kurva eliptik `SECP256k1`, pembuatan alamat, tanda tangan digital ECDSA, dan verifikasi keabsahan transaksi.
9. **`level08_jaringan.py` & `level08_server.py`** — Simulasi jaringan multi-node *peer-to-peer*, penyiaran blok (*broadcast*), *fork*, dan konsensus rantai terpanjang (`resolve_conflicts`).
10. **`level09_reward_saldo.py`** — Transaksi *coinbase* (`MINING_REWARD`), perhitungan saldo model akun, total suplai, dan `validasi_ekonomi`.
11. **`tugas_personal_2/`** — Modifikasi Level 6–9 menggunakan data pribadi mahasiswa (`data_saya.py`, `modifikasi_2.py`, `skenario_2.py`, `jalankan_tugas_2.py`).
- **Laporan Analisis Materi 6–9:**
  - [`laporan_tugas_personal_Materi 6 - 9.md`](./laporan_tugas_personal_Materi%206%20-%209.md)
  - [`tugas_personal_2/laporan_tugas_personal_2_2067.md`](./tugas_personal_2/laporan_tugas_personal_2_2067.md)

---

## Cara Menjalankan

```bash
# Menjalankan seluruh unit test (Level 1 - 9)
pytest -v

# Menjalankan Tugas Personal 1 (Level 1 - 5) dan Tugas Personal 2 (Level 6 - 9)
python tugas_personal/jalankan_tugas.py
python tugas_personal_2/jalankan_tugas_2.py
```
