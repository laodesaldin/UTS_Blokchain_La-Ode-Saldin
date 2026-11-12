# Laporan Tugas Personal 2 — Blockchain Level 6–9

- **Nama:** LA ODE SALDIN
- **NIM (4 digit terakhir):** 2067
- **Dibuat:** 2026-11-12 23:14  (waktu proses 0.1 detik)
- **Kode verifikasi:** `65F2D611A0D0`

> Bagian hasil dibuat otomatis. Jangan diubah: dosen menghitung ulang semua angka dari data Anda.
> Isi bagian **Analisis** dengan kata-kata Anda sendiri.

## Level 6 — Mining data pribadi dan jejak difficulty

Data yang ditambang: `LA ODE SALDIN|2067|2004-01-08`

| Difficulty | Nonce | Percobaan | Teori 16^d | Hash |
|---|---|---|---|---|
| 1 | 42 | 43 | 16 | `00afcb2433015ce22aee…` |
| 2 | 42 | 43 | 256 | `00afcb2433015ce22aee…` |
| 3 | 2398 | 2.399 | 4.096 | `0006aca24045ba6a575a…` |
| 4 | 17398 | 17.399 | 65.536 | `0000b6045d764c960489…` |

- Difficulty awal (dari NIM): **4**, target waktu blok 10 detik
- Waktu blok simulasi (dari NIM + tanggal + bulan lahir): 8, 0, 24, 28, 0, 32, 0, 4 detik
- Jejak difficulty (Modifikasi 6): **4, 5, 4, 3, 4, 3, 4, 5**

## Level 7 — Kunci dan tanda tangan dari data pribadi

- Kunci publik (32 karakter awal): `2b5abf63c3602778f71aee274bd63771…`
- Alamat Anda: `fd7e1351a10247bd351f42abcce954b463cac226`
- Transaksi: kirim **8** ke TEMAN_A
- Tanda tangan: `af9d73513fdb2643eaf0a647bc7c9f5128657e824a66d30f…`
- Tanda tangan selalu sama saat diulang: True
- Transaksi sah: **True**; setelah amount diubah: **False**
- Penipu memakai alamat Anda: tanda tangannya valid dengan kuncinya = True, transaksinya sah = **False**

## Level 8 — Jaringan dan fork pribadi

- Jumlah node: **3**; blok pribadi tiap node: [3, 1, 1]
- Panjang rantai saat fork: [5, 3, 3]
- Setelah resolve_conflicts: [5, 5, 5], sepakat = **True**
- Pemenang fork: **LA-1**; blok terbuang (orphan): **2**
- Hash ujung rantai: `00affaec5e971b6e7ba153c7…`

## Level 9 — Ekonomi dengan halving

- Hadiah awal: **47**, halving setiap **2** blok
- Hadiah blok 1–6 (Modifikasi 9): **47, 47, 23, 23, 11, 11**

| Alamat | Saldo |
|---|---|
| LA ODE SALDIN | 123 |
| TEMAN_A | 21 |
| TEMAN_B | 18 |

- Total suplai: **162**
- Belanja melebihi saldo ditolak: True
- Validasi ekonomi: **True**; setelah hadiah blok 1 dicurangi: **False**

## Analisis (isi dengan kata-kata Anda sendiri)

1. **Level 6.** Bandingkan kolom Percobaan dengan Teori 16^d pada tabel Anda. Mengapa bisa berbeda jauh? Lalu jelaskan jejak difficulty Anda (4, 5, 4, 3, 4, 3, 4, 5): pada langkah mana difficulty naik, tetap, dan turun, dan mengapa?

   _Jawaban:_
   Pada tabel hasil mining data pribadi `LA ODE SALDIN|2067|2004-01-08`, terlihat perbedaan antara jumlah **Percobaan** aktual dan **Teori $16^d$**:
   - **Difficulty 1:** Percobaan aktual = `43`, sedangkan teori $16^1 = 16$.
   - **Difficulty 2:** Percobaan aktual = `43`, sedangkan teori $16^2 = 256$ (kebetulan pada `nonce = 42`, nilai hash `00afcb24...` sudah langsung memiliki dua angka nol di depan, sehingga memenuhi syarat difficulty 1 sekaligus difficulty 2).
   - **Difficulty 3:** Percobaan aktual = `2.399`, sedangkan teori $16^3 = 4.096$.
   - **Difficulty 4:** Percobaan aktual = `17.399`, sedangkan teori $16^4 = 65.536$.

   **Mengapa bisa berbeda jauh?** Nilai $16^d$ adalah **ekspektasi matematis (rata-rata teoretis jangka panjang)** dari distribusi probabilitas geometris di mana peluang setiap tebakan menghasilkan `d` karakter heksadesimal nol di awal adalah $(1/16)^d$. Karena keluaran SHA-256 bersifat acak semu (*pseudo-random*) dan kita hanya menguji **satu sampel data** (`n = 1`), hasil aktualnya memiliki variansi yang tinggi (bisa jauh lebih cepat karena "beruntung" menemukan nonce lebih awal seperti pada difficulty 2, 3, dan 4, atau sedikit lebih lama seperti pada difficulty 1). Jika percobaan diulang ratusan/ribuan kali dengan input berbeda lalu dirata-ratakan, barulah rata-rata percobaannya mendekati $16^d$.

   **Penjelasan Jejak Difficulty (`4, 5, 4, 3, 4, 3, 4, 5`):**
   Dengan `difficulty_awal = 4` dan `target_detik = 10` detik, aturan `sesuaikan_difficulty` adalah:
   - Jika `waktu_aktual < 5` detik (`< target / 2`) $\rightarrow$ difficulty **naik 1**.
   - Jika `waktu_aktual > 20` detik (`> target * 2`) $\rightarrow$ difficulty **turun 1** (minimal 1).
   - Jika `5 <= waktu_aktual <= 20` detik $\rightarrow$ difficulty **tetap**.

   Rincian langkah demi langkah untuk deret waktu `[8, 0, 24, 28, 0, 32, 0, 4]` detik:
   1. **Langkah 1 (`8` detik):** Karena $5 \le 8 \le 20$ (wajar), difficulty **tetap** dari `4` menjadi **`4`**.
   2. **Langkah 2 (`0` detik):** Karena $0 < 5$ (terlalu cepat), difficulty **naik 1** dari `4` menjadi **`5`**.
   3. **Langkah 3 (`24` detik):** Karena $24 > 20$ (terlalu lambat), difficulty **turun 1** dari `5` menjadi **`4`**.
   4. **Langkah 4 (`28` detik):** Karena $28 > 20$ (terlalu lambat), difficulty **turun 1** dari `4` menjadi **`3`**.
   5. **Langkah 5 (`0` detik):** Karena $0 < 5$ (terlalu cepat), difficulty **naik 1** dari `3` menjadi **`4`**.
   6. **Langkah 6 (`32` detik):** Karena $32 > 20$ (terlalu lambat), difficulty **turun 1** dari `4` menjadi **`3`**.
   7. **Langkah 7 (`0` detik):** Karena $0 < 5$ (terlalu cepat), difficulty **naik 1** dari `3` menjadi **`4`**.
   8. **Langkah 8 (`4` detik):** Karena $4 < 5$ (terlalu cepat), difficulty **naik 1** dari `4` menjadi **`5`**.

2. **Level 7.** Mengapa tanda tangan Anda selalu sama setiap kali program dijalankan, padahal di Level 7 asli berubah-ubah? Mengapa transaksi penipu tidak sah walaupun tanda tangannya valid?

   _Jawaban:_
   - **Mengapa tanda tangan selalu sama:** Pada Level 7 asli (`SigningKey.sign`), algoritma ECDSA standar membangkitkan bilangan acak sementara (*ephemeral random nonce* $k$) yang baru setiap kali melakukan penandatanganan, sehingga transaksi dan kunci privat yang sama menghasilkan tanda tangan yang selalu berbeda setiap kali program dijalankan. Sebaliknya, pada Modifikasi 7 kita menggunakan:
     1. `kunci_dari_data()` yang menurunkan kunci privat secara deterministik dari hash `SHA-256("2067:LA ODE SALDIN:2004-01-08")`, dan
     2. `SigningKey.sign_deterministic()` (standar **RFC 6979**) yang menurunkan nilai $k$ secara deterministik dari kunci privat dan hash pesan transaksi. Karena tidak ada komponen acak sama sekali, tanda tangan yang dihasilkan selalu identik (`af9d73513fdb2643...`).
   - **Mengapa transaksi penipu tidak sah walaupun tanda tangannya valid:** Pada skenario penipuan, penipu membuat transaksi dengan mengklaim `sender = "fd7e1351a10247bd351f42abcce954b463cac226"` (alamat milik saya), lalu menandatanganinya menggunakan kunci privat milik penipu sendiri (`priv_t`). Saat diuji dengan `verifikasi(tx_curian, ttd_curian, pub_t)`, hasilnya **`True`** karena secara matematis tanda tangan tersebut memang cocok dengan kunci publik penipu (`pub_t`). Namun, ketika diuji dengan `transaksi_sah()`, hasilnya **`False`** karena fungsi `transaksi_sah()` memeriksa kecocokan kepemilikan: `alamat_dari_kunci_publik(pub_t)` menghasilkan alamat milik penipu, yang **tidak sama** dengan alamat `sender` pada transaksi. Dengan demikian, seseorang tidak bisa membelanjakan koin milik alamat orang lain menggunakan pasangan kuncinya sendiri.

3. **Keamanan kunci.** Kunci privat Anda dibuat dari nama, NIM, dan tanggal lahir. Mengapa cara ini SANGAT BERBAHAYA di dunia nyata? Siapa saja yang bisa mencuri dana alamat Anda? (Cari tahu istilah *brain wallet*.)

   _Jawaban:_
   Metode membuat kunci privat secara langsung dari hash kata sandi, kalimat, atau data pribadi yang mudah diingat manusia dikenal dengan istilah ***brain wallet***. Cara ini **sangat berbahaya** di dunia nyata karena:
   1. **Entropi (keacakan) sangat rendah:** Berbeda dengan kunci acak 256-bit sejati yang memiliki $\approx 1,15 \times 10^{77}$ kemungkinan, kombinasi nama, 4 digit NIM, dan tanggal lahir memiliki ruang tebakan yang sangat sempit dan mudah diprediksi.
   2. **Rentan terhadap serangan *dictionary / brute-force* otomatis:** Di jaringan blockchain nyata (seperti Bitcoin dan Ethereum), terdapat bot pemindai otomatis yang terus-menerus menghitung hash dari jutaan kombinasi nama, tanggal lahir, kata kamus, dan data bocoran untuk langsung menguras saldo begitu ada dana masuk ke alamat *brain wallet*.
   3. **Siapa saja yang bisa mencuri dana alamat saya:** Siapa pun yang mengetahui atau dapat mencari biodata saya—seperti teman kuliah, dosen, staf akademik, orang yang melihat daftar hadir/KRS/KTM, maupun pihak luar yang menemukan profil media sosial saya (Nama: `LA ODE SALDIN`, NIM: `2067`, Tanggal Lahir: `2004-01-08`)—dapat dengan mudah menjalankan fungsi hash yang sama untuk menghasilkan kunci privat saya dan mencuri seluruh koin di alamat `fd7e1351a10247bd351f42abcce954b463cac226`.

4. **Level 8.** Jaringan Anda punya 3 node dan pemenangnya LA-1 dengan 2 blok terbuang. Jelaskan mengapa node itu menang. Cari teman yang jaringannya sempat tidak sepakat: apa penyebabnya dan bagaimana diselesaikan?

   _Jawaban:_
   - **Mengapa node `LA-1` menang dan ada 2 blok terbuang:**
     Berdasarkan `NIM_4 = 2067`, jumlah node adalah `3 + (2067 % 3) = 3` node (`LA-1`, `LA-2`, `LA-3`). Sebelum *fork*, ketiganya sudah memiliki **2 blok yang sama** (Blok `#0` genesis dan Blok `#1` pembuka jaringan). Dari digit pribadi `20670801`, tiga digit pertama adalah `2`, `0`, `6`, sehingga jumlah blok pribadi yang ditambang masing-masing node tanpa disiarkan adalah:
     - `LA-1`: `1 + (2 % 3) = 3` blok pribadi $\rightarrow$ total panjang rantai = `2 + 3 = 5` blok.
     - `LA-2`: `1 + (0 % 3) = 1` blok pribadi $\rightarrow$ total panjang rantai = `2 + 1 = 3` blok.
     - `LA-3`: `1 + (6 % 3) = 1` blok pribadi $\rightarrow$ total panjang rantai = `2 + 1 = 3` blok.
     Saat `resolve_conflicts()` dijalankan, aturan konsensus **rantai valid terpanjang (*longest valid chain*)** membuat `LA-2` dan `LA-3` mengganti rantai mereka (panjang 3) dengan rantai milik **`LA-1`** yang paling panjang (panjang 5). Akibatnya, seluruh node langsung sepakat (`[5, 5, 5]`), dan blok pribadi milik `LA-2` (1 blok) serta `LA-3` (1 blok) tidak lagi dipakai sehingga terdapat **`1 + 1 = 2` blok terbuang (*orphan/stale blocks*)**.
   - **Kasus teman yang jaringannya sempat tidak sepakat (`sepakat_setelah_resolve = False`):**
     Hal itu terjadi ketika saat *fork*, terdapat **dua atau lebih node yang memiliki rantai terpanjang dengan panjang yang sama persis (seri / *tie*)**, misalnya panjang rantai saat *fork* adalah `[4, 4, 3]` atau `[5, 5, 3]`. Karena fungsi `resolve_conflicts()` hanya mengganti rantai lokal apabila rantai peer **lebih panjang (`>`)** dari rantai sendiri (bukan sama panjang `==`), maka kedua node yang seri sama-sama mempertahankan cabang versinya masing-masing. Ketidaksepakatan ini diselesaikan ketika salah satu node (`nodes[0]`) menambang dan menyiarkan **1 blok pemecah seri (*tie-breaker block*)**, sehingga rantai node tersebut bertambah panjang 1 blok menjadi satu-satunya rantai terpanjang, dan panggilan `resolve_conflicts()` berikutnya membuat seluruh jaringan sepakat bulat.

5. **Level 9.** Dengan hadiah awal 47 dan halving setiap 2 blok, berapa batas total suplai jika mining berjalan selamanya? Tunjukkan perhitungannya, lalu kaitkan dengan batas 21 juta Bitcoin.

   _Jawaban:_
   Berdasarkan `NIM_4 = 2067`, diperoleh `hadiah_awal = 20 + (2067 % 30) = 47` dan `interval_halving = 2 + (2067 % 3) = 2` blok. Rumus hadiah per blok pada `BlockchainHalving` menggunakan pembagian bulat (`//`):
   $$\text{hadiah}(\text{index}) = 47 \mathbin{//} 2^{\lfloor(\text{index}-1)/2\rfloor}$$
   Jika penambangan berjalan selamanya, rincian koin baru yang tercipta pada setiap periode halving (masing-masing 2 blok) adalah:
   - **Periode ke-1 (Blok 1 – 2):** $\text{hadiah} = 47 // 2^0 = 47 \implies 2 \times 47 = 94$ koin
   - **Periode ke-2 (Blok 3 – 4):** $\text{hadiah} = 47 // 2^1 = 23 \implies 2 \times 23 = 46$ koin
   - **Periode ke-3 (Blok 5 – 6):** $\text{hadiah} = 47 // 2^2 = 11 \implies 2 \times 11 = 22$ koin *(total suplai s/d blok 6 = $94 + 46 + 22 = 162$ koin, sesuai laporan)*
   - **Periode ke-4 (Blok 7 – 8):** $\text{hadiah} = 47 // 2^3 = 5 \implies 2 \times 5 = 10$ koin
   - **Periode ke-5 (Blok 9 – 10):** $\text{hadiah} = 47 // 2^4 = 2 \implies 2 \times 2 = 4$ koin
   - **Periode ke-6 (Blok 11 – 12):** $\text{hadiah} = 47 // 2^5 = 1 \implies 2 \times 1 = 2$ koin
   - **Periode ke-7 dst. (Blok 13+):** $\text{hadiah} = 47 // 2^6 = 0 \implies 0$ koin selamanya.

   Maka **batas total suplai maksimum** (dengan pembagian bulat `//`) jika mining berjalan selamanya adalah:
   $$\text{Total Suplai Maksimum} = 94 + 46 + 22 + 10 + 4 + 2 = \mathbf{178\text{ koin}}$$
   *(Sebagai perbandingan, jika tanpa pembulatan integer / deret geometri tak hingga $S_\infty = \frac{a}{1 - r}$ dengan $a = 2 \times 47 = 94$ dan $r = \frac{1}{2}$, maka batas teoretisnya adalah $\frac{94}{1 - 0,5} = 188$ koin).*

   **Kaitan dengan batas 21 juta Bitcoin:**
   Model ini adalah tiruan langsung dari mekanisme *halving* pada protokol Bitcoin. Bitcoin memulai blok genesisnya dengan hadiah awal **50 BTC per blok**, dan hadiah tersebut dipotong separuh (*halving*) setiap **210.000 blok** (sekitar 4 tahun sekali dengan target waktu blok 10 menit): $50 \to 25 \to 12,5 \to 6,25 \to 3,125 \text{ BTC}$, dan seterusnya. Dengan menjumlahkan deret geometri tersebut:
   $$\text{Total BTC} = 210.000 \times 50 \times \sum_{k=0}^{\infty} \left(\frac{1}{2}\right)^k = 210.000 \times 50 \times 2 = \mathbf{21.000.000\text{ BTC}}$$
   Sama seperti pembagian bulat `//` pada kode Python kita yang akhirnya membuat hadiah menjadi `0` setelah blok ke-12, di Bitcoin satuan terkecil adalah 1 *satoshi* ($10^{-8}$ BTC) dan operasi pembagian hadiah menggunakan *bit-shift* bulat (`>> 1`), sehingga setelah *halving* ke-33 (sekitar tahun 2140), hadiah blok Bitcoin menjadi 0 dan total suplainya tidak akan pernah melebihi **21 juta BTC** (tepatnya $20.999.999,9769\text{ BTC}$). Mekanisme ini menjamin Bitcoin bersifat langka (*scarce*) dan tahan terhadap inflasi berlebih.

---

## Data verifikasi (JANGAN DIUBAH)

<!-- DATA-VERIFIKASI -->
```json
{
  "tugas": "personal-2 (Level 6-9)",
  "profil": {
    "nama": "LA ODE SALDIN",
    "nim4": "2067",
    "tanggal_lahir": "2004-01-08",
    "kota_asal": "Kab. Muna",
    "hobi": "Gamer"
  },
  "level6": {
    "data_ditambang": "LA ODE SALDIN|2067|2004-01-08",
    "mining": [
      {
        "difficulty": 1,
        "nonce": 42,
        "hash": "00afcb2433015ce22aee23566a697762c45508d1e0bf0bb7b0bb196acdc22e81",
        "percobaan": 43,
        "teori": 16
      },
      {
        "difficulty": 2,
        "nonce": 42,
        "hash": "00afcb2433015ce22aee23566a697762c45508d1e0bf0bb7b0bb196acdc22e81",
        "percobaan": 43,
        "teori": 256
      },
      {
        "difficulty": 3,
        "nonce": 2398,
        "hash": "0006aca24045ba6a575a5649321eeab11fe11485c87e55b032d2ffe673e22e4e",
        "percobaan": 2399,
        "teori": 4096
      },
      {
        "difficulty": 4,
        "nonce": 17398,
        "hash": "0000b6045d764c960489b0c7a652abbf2edeb352f4309102f645064d60f446bb",
        "percobaan": 17399,
        "teori": 65536
      }
    ],
    "difficulty_awal": 4,
    "daftar_waktu_detik": [
      8,
      0,
      24,
      28,
      0,
      32,
      0,
      4
    ],
    "target_detik": 10,
    "jejak_difficulty": [
      4,
      5,
      4,
      3,
      4,
      3,
      4,
      5
    ]
  },
  "level7": {
    "kunci_publik_awal": "2b5abf63c3602778f71aee274bd63771",
    "alamat": "fd7e1351a10247bd351f42abcce954b463cac226",
    "transaksi": {
      "sender": "fd7e1351a10247bd351f42abcce954b463cac226",
      "recipient": "TEMAN_A",
      "amount": 8
    },
    "tanda_tangan": "af9d73513fdb2643eaf0a647bc7c9f5128657e824a66d30f1bdde3c37ad91358177c9e064d7cee46add895bdf81ce18a663fdc51d5c3c2bf74a95d363fb9e00d",
    "tanda_tangan_selalu_sama": true,
    "sah": true,
    "sah_setelah_amount_diubah": false,
    "ttd_penipu_valid_dengan_kuncinya": true,
    "transaksi_penipu_sah": false
  },
  "level8": {
    "jumlah_node": 3,
    "blok_pribadi_per_node": [
      3,
      1,
      1
    ],
    "panjang_saat_fork": [
      5,
      3,
      3
    ],
    "panjang_setelah_resolve": [
      5,
      5,
      5
    ],
    "sepakat_setelah_resolve": true,
    "perlu_pemecah_seri": false,
    "pemenang_fork": "LA-1",
    "blok_terbuang": 2,
    "hash_ujung": "00affaec5e971b6e7ba153c7eeda412bfa8e596d2e073810f0fd94d0b3c4f6da"
  },
  "level9": {
    "hadiah_awal": 47,
    "interval_halving": 2,
    "hadiah_per_blok": [
      47,
      47,
      23,
      23,
      11,
      11
    ],
    "saldo": {
      "LA ODE SALDIN": 123,
      "TEMAN_A": 21,
      "TEMAN_B": 18
    },
    "total_suplai": 162,
    "belanja_melebihi_saldo_ditolak": true,
    "validasi_ekonomi": true,
    "hash_ujung": "007252b878cd84049d9a66f9b58ad996f5cac6a57b7eb08835c599f23381700b",
    "validasi_setelah_hadiah_dicurangi": false
  },
  "kode_verifikasi": "65F2D611A0D0"
}
```
