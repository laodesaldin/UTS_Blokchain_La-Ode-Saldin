# Laporan Tugas Personal Blockchain Level 1–5

- **Nama:** LA ODE SALDIN
- **NIM (4 digit terakhir):** 2067
- **Dibuat:** 2026-11-12 23:23  (waktu proses 3.1 detik)
- **Kode verifikasi:** `D95E30877452`

> Bagian hasil dibuat otomatis. Jangan diubah: dosen menghitung ulang semua angka dari data Anda.
> Isi bagian **Analisis** dengan kata-kata Anda sendiri.

## Level 1 — Hash data pribadi

| Hasil | Nilai |
|---|---|
| SHA-256 nama | `6335f099dca589f54eff5975889b4e7baad2aad8465c5467aa29d08b9bab3153` |
| hash_dict profil | `c555d99c7faa959de38ded1d92c5c2abae8246cf8c27cd7cf5f3fd1040cf7972` |
| hash_dict profil (urutan key dibalik) | `c555d99c7faa959de38ded1d92c5c2abae8246cf8c27cd7cf5f3fd1040cf7972` |
| Bit berubah: tanggal lahir vs tanggal lahir + 1 hari | 47.27% |
| ID mahasiswa (Modifikasi 1) | `10804710` |

## Level 2 — Blockchain personal

- Proof genesis: **2067** (dari NIM)
- Proof blok 2, 3, 4: **98577, 79151, 118102**
- Pemilik setiap blok: `10804710`
- Rantai valid: True

## Level 3 — Pemalsuan data pribadi

- Posisi yang dipalsukan: **4**
- Data asli: `LA ODE SALDIN NIM akhir 2067`
- Data palsu: `LA ODE SALDIN NIM akhir 2067 (DIPALSUKAN)`
- Valid sebelum dipalsukan: True
- Tautan putus di indeks: **None**
- Valid setelah dipalsukan: **True**
- Valid setelah disambung ulang: **True**

## Level 4 — Transaksi dari data pribadi

| Blok | Pengirim | Penerima | Jumlah |
|---|---|---|---|
| 2 | LA ODE SALDIN | TEMAN_A | 8 |
| 2 | TEMAN_A | LA ODE SALDIN | 1 |
| 3 | LA ODE SALDIN | DOSEN | 18 |

- Ringkasan saldo (Modifikasi 4): masuk **1**, keluar **26**, bersih **-25**
- Kirim ke diri sendiri ditolak: True
- Amount 0 ditolak: True

## Level 5 — Proof of Work dengan nonce (deterministik)

| Blok | Nonce | Hash |
|---|---|---|
| 0 | 133144 | `0000c0054f7d4f74a4bc0956…` |
| 1 | 90447 | `00000946bccbeb5a1503ebaa…` |
| 2 | 47935 | `0000dd2982540d630dfb395f…` |
| 3 | 37830 | `00003440905161d756599801…` |

- Valid: True → setelah blok 1 dipalsukan: **False**
- Percobaan hash untuk menambang ulang blok 1–3: **226.306**
- Valid setelah ditambang ulang: True

## Analisis (isi dengan kata-kata Anda sendiri)

1. **Level 1.** Bandingkan SHA-256 nama Anda dengan milik seorang teman. Apakah ada pola yang mirip? Jelaskan juga mengapa dua hash profil Anda sama, dan mengapa hanya menambah 1 hari pada tanggal lahir mengubah 47.27% bit.

   _Jawaban:_
   - **Perbandingan SHA-256 nama dengan teman:** Hash SHA-256 nama saya (`LA ODE SALDIN` $\rightarrow$ `6335f099dca589f5...`) sama sekali tidak memiliki pola kemiripan dengan hash nama teman, meskipun ada teman yang memiliki awalan marga yang sama (misalnya sama-sama diawali `"LA ODE ..."`). Hal ini karena fungsi hash kriptografis mendistribusikan bit keluaran secara acak semu (*pseudo-random*) dan seragam untuk setiap input yang berbeda.
   - **Mengapa dua hash profil sama (`c555d99c7faa959d...`):** Meskipun urutan key pada `profil_terbalik` dibalik (`dict(reversed(list(p.items())))`), fungsi `hash_dict()` menggunakan serialisasi kanonik `json.dumps(data, sort_keys=True)`. Opsi `sort_keys=True` selalu mengurutkan key secara alfabetis sebelum diubah menjadi teks JSON, sehingga string yang di-hash tetap identik.
   - **Mengapa menambah 1 hari pada tanggal lahir (`2004-01-08` $\rightarrow$ `2004-01-09`) mengubah `47.27%` bit:** Ini adalah bukti nyata dari **efek longsoran (*avalanche effect*)** pada SHA-256. Mengubah satu karakter saja (`'8'` menjadi `'9'`) menyebabkan reaksi berantai pada operasi bitwise internal SHA-256 sehingga hampir separuh bit keluaran (`121` dari `256` bit, atau `47.27%`, mendekati ideal teoretis `~50%`) berubah secara drastis.

2. **Level 2.** Kode Anda dan teman sama persis, tetapi proof Anda (98577, 79151, 118102) berbeda. Jelaskan penyebabnya.

   _Jawaban:_
   Penyebabnya adalah pada `BlockchainPersonal` (Modifikasi 2), nilai **`proof` pada blok genesis diatur sama dengan 4 digit terakhir NIM masing-masing mahasiswa** (`proof_genesis = int("2067") = 2067`), bukan angka tetap `1` seperti di kode asli. Karena rumus Proof of Work Level 2 adalah mencari `proof` terkecil sehingga `SHA-256(str(proof² - previous_proof²))` diawali `"0000"`, maka:
   - Nilai `proof` Blok #2 (`98577`) bergantung langsung pada `proof` Blok #1 (`2067`).
   - Nilai `proof` Blok #3 (`79151`) bergantung pada `proof` Blok #2 (`98577`).
   - Nilai `proof` Blok #4 (`118102`) bergantung pada `proof` Blok #3 (`79151`).
   Akibat ketergantungan berantai ini, perbedaan nilai awal `proof_genesis` dari NIM membuat seluruh deret `proof` blok berikutnya unik untuk setiap mahasiswa.

3. **Level 3.** Anda memalsukan posisi 4 dan tidak ada tautan putus yang terdeteksi (None), sedangkan valid setelah dipalsukan = True. Jelaskan hasil ini, lalu bandingkan dengan teman yang posisi pemalsuannya berbeda.

   _Jawaban:_
   - **Mengapa `tautan_putus_di = None` dan `valid_setelah_dipalsukan = True` pada posisi 4:**
     Berdasarkan `NIM_4 = 2067`, posisi blok yang dipalsukan adalah `1 + (2067 % 4) = 1 + 3 = 4`. Karena rantai memiliki total 5 blok (indeks `0` s/d `4`), maka **indeks `4` adalah blok paling terakhir (ujung/ekor rantai)**.
     1. Fungsi `cari_tautan_putus` hanya memeriksa apakah `chain[i]["previous_hash"] == hash_blok(chain[i-1])`. Karena tidak ada blok ke-5 (`i = 5`) setelah indeks `4` yang menyimpan hash blok ke-4, maka tidak ada tautan `previous_hash` yang putus (`None`).
     2. Pada desain Level 3 (gaya GeeksforGeeks), blok tidak menyimpan hash dirinya sendiri dan fungsi `valid_proof` hanya memeriksa `proof² - previous_proof²` tanpa melibatkan field `data`. Akibatnya, pemalsuan pada blok terakhir (`posisi = 4`) **sama sekali tidak terdeteksi** oleh `chain_valid(palsu)` sehingga langsung bernilai **`True`** bahkan sebelum disambung ulang!
   - **Perbandingan dengan teman yang posisi pemalsuannya berbeda (posisi 1, 2, atau 3):**
     Teman yang `1 + (NIM_4 % 4)`-nya menghasilkan posisi `1`, `2`, atau `3` memalsukan blok di **tengah rantai**. Pada kasus mereka, perubahan `data` di posisi `k` mengubah `hash_blok(chain[k])`, sehingga blok sesudahnya (`posisi + 1`) langsung terdeteksi putus oleh `cari_tautan_putus` (melaporkan indeks `k + 1`) dan `valid_setelah_dipalsukan` bernilai **`False`**. Rantai mereka baru kembali bernilai `True` setelah dijalankan `sambung_ulang`.

4. **Level 4.** Jelaskan dari mana angka masuk 1, keluar 26, dan bersih -25 berasal. Mengapa transaksi ke diri sendiri perlu ditolak?

   _Jawaban:_
   - **Asal-usul angka `masuk = 1`, `keluar = 26`, dan `bersih = -25`:**
     Dari `TANGGAL_LAHIR = "2004-01-08"` (`hari = 8`, `bulan = 1`) dan `NIM_4 = 2067`, fungsi `transaksi_personal()` membuat 3 transaksi yang sudah ditambang ke dalam blok:
     1. Blok #2: `LA ODE SALDIN -> TEMAN_A` sebesar `hari = 8` (**keluar 8**).
     2. Blok #2: `TEMAN_A -> LA ODE SALDIN` sebesar `bulan = 1` (**masuk 1**).
     3. Blok #3: `LA ODE SALDIN -> DOSEN` sebesar `(2067 % 50) + 1 = 17 + 1 = 18` (**keluar 18**).
     Sehingga:
     - Total **masuk** = `1`
     - Total **keluar** = `8 + 18 = 26`
     - Saldo **bersih** = `masuk - keluar = 1 - 26 = -25`.
   - **Mengapa transaksi ke diri sendiri (`sender == recipient`) perlu ditolak:**
     Secara ekonomi transaksi ke diri sendiri tidak mengubah saldo bersih, namun membebani ruang penyimpanan blok dan mempool (dapat disalahgunakan untuk serangan *spamming* transaksi palsu atau memanipulasi volume transaksi secara semu), serta berisiko menimbulkan bug perhitungan ganda jika fungsi penghitung saldo tidak memisahkan pengirim dan penerima dengan hati-hati.

5. **Level 5.** Penyerang butuh 226.306 percobaan hash untuk memalsukan rantai Anda. Mengapa nonce Anda selalu sama setiap kali program dijalankan, padahal di demo Level 5 asli nonce berubah-ubah?

   _Jawaban:_
   - Di Level 5 asli, setiap blok menggunakan `datetime.datetime.now()` sebagai `timestamp`. Karena waktu komputer terus berjalan hingga satuan mikrodetik setiap kali program dieksekusi, isi JSON blok selalu berbeda, sehingga nilai `nonce` yang menghasilkan hash berawalan `"0000"` juga selalu berubah-ubah.
   - Sebaliknya, pada `BlockchainDeterministik` (Modifikasi 5), jam komputer dihilangkan dan diganti dengan string tetap dari tanggal lahir: `"2004-01-08"` untuk blok genesis dan `f"2004-01-08 #{index}"` untuk blok berikutnya, serta daftar transaksi berasal dari data diri yang tetap. Karena seluruh field di dalam blok bersifat deterministik (selalu sama persis), maka pencarian `nonce` dari `0, 1, 2, ...` akan selalu menemukan nilai `nonce` yang sama (`[133144, 90447, 47935, 37830]`) dan membutuhkan jumlah percobaan tambang ulang yang selalu sama (`226.306` percobaan hash untuk menambang ulang Blok #1, #2, dan #3).

6. **Etika data.** Anda baru saja menyimpan nama dan tanggal lahir di dalam blockchain. Jika ini blockchain publik, apa risikonya? Kaitkan dengan sifat immutability dan UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi, terutama hak untuk menghapus data.

   _Jawaban:_
   Menyimpan data pribadi secara mentah (*plaintext*) seperti Nama Lengkap, NIM, dan Tanggal Lahir di dalam **blockchain publik** menimbulkan risiko privasi dan keamanan yang sangat serius:
   1. **Risiko Keamanan & Privasi:** Semua node dan publik di seluruh dunia dapat membaca salinan buku besar blockchain selamanya. Data tersebut dapat disalahgunakan untuk pencurian identitas (*identity theft*), pembuatan profil (*profiling*), hingga rekayasa sosial (*social engineering*).
   2. **Konflik antara *Immutability* dan UU PDP (UU No. 27 Tahun 2022):**
      - Salah satu pilar utama teknologi blockchain adalah ***immutability* (kekekalan data)**: begitu sebuah blok ditambang dan tertanam di dalam rantai, datanya tidak dapat diubah atau dihapus tanpa merusak hash seluruh blok sesudahnya dan mengulang Proof of Work mayoritas jaringan.
      - Di sisi lain, **UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP)** (khususnya Pasal 8 dan Pasal 43–44 tentang **Hak untuk Dihapus / *Right to Erasure / Right to be Forgotten***) memberikan hak hukum kepada Subjek Data Pribadi untuk meminta penghapusan atau pemusnahan data pribadinya apabila tidak lagi diperlukan atau persetujuan ditarik.
      - Jika data pribadi disimpan langsung di dalam blok (*on-chain*), penyelenggara sistem tidak akan bisa menghapus data tersebut secara teknis, sehingga melanggar ketentuan UU PDP. Solusi arsitektur blockchain yang benar adalah **tidak pernah menyimpan data pribadi mentah secara *on-chain***, melainkan menyimpannya di basis data *off-chain* (yang bisa dihapus) dan hanya menyimpan **komitmen hash kriptografis (*hash pointer* / *salted hash*)** di dalam blockchain.

---

## Data verifikasi (JANGAN DIUBAH)

<!-- DATA-VERIFIKASI -->
```json
{
  "profil": {
    "nama": "LA ODE SALDIN",
    "nim4": "2067",
    "tanggal_lahir": "2004-01-08",
    "kota_asal": "Kab. Muna",
    "hobi": "Gamer"
  },
  "level1": {
    "hash_nama": "6335f099dca589f54eff5975889b4e7baad2aad8465c5467aa29d08b9bab3153",
    "hash_profil": "c555d99c7faa959de38ded1d92c5c2abae8246cf8c27cd7cf5f3fd1040cf7972",
    "hash_profil_urutan_terbalik": "c555d99c7faa959de38ded1d92c5c2abae8246cf8c27cd7cf5f3fd1040cf7972",
    "avalanche_tanggal_persen": 47.27,
    "id_mahasiswa": "10804710"
  },
  "level2": {
    "proof_genesis": 2067,
    "proof_blok": [
      98577,
      79151,
      118102
    ],
    "pemilik_semua_blok": [
      "10804710"
    ],
    "valid": true
  },
  "level3": {
    "posisi_dipalsukan": 4,
    "data_asli": "LA ODE SALDIN NIM akhir 2067",
    "data_palsu": "LA ODE SALDIN NIM akhir 2067 (DIPALSUKAN)",
    "valid_asli": true,
    "tautan_putus_di": null,
    "valid_setelah_dipalsukan": true,
    "valid_setelah_disambung_ulang": true
  },
  "level4": {
    "riwayat": [
      [
        2,
        {
          "sender": "LA ODE SALDIN",
          "recipient": "TEMAN_A",
          "amount": 8
        }
      ],
      [
        2,
        {
          "sender": "TEMAN_A",
          "recipient": "LA ODE SALDIN",
          "amount": 1
        }
      ],
      [
        3,
        {
          "sender": "LA ODE SALDIN",
          "recipient": "DOSEN",
          "amount": 18
        }
      ]
    ],
    "ringkasan_saldo": {
      "masuk": 1,
      "keluar": 26,
      "bersih": -25
    },
    "kirim_ke_diri_sendiri_ditolak": true,
    "amount_nol_ditolak": true,
    "jumlah_blok": 3
  },
  "level5": {
    "nonce": [
      133144,
      90447,
      47935,
      37830
    ],
    "hash": [
      "0000c0054f7d4f74a4bc0956002cf4acb20b5c9f6dd4dcf6c72afd996bdcb365",
      "00000946bccbeb5a1503ebaadea277b606ae75321fc22a784c0237ee4e1fc641",
      "0000dd2982540d630dfb395f6f5d8c756533cc1265c5939c88f95993bb930391",
      "00003440905161d756599801e3d61d1090f7d3420c9cc9b76c4a84d376c6b278"
    ],
    "valid": true,
    "valid_setelah_dipalsukan": false,
    "percobaan_tambang_ulang": 226306,
    "valid_setelah_tambang_ulang": true
  },
  "kode_verifikasi": "D95E30877452"
}
```
