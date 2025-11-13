# Analisis 07: Basic Web Handling With Views

## 1. Tujuan Percobaan
Melakukan refaktor kode untuk memisahkan *concern*. Logika *view* (yang menangani *request*) dipindahkan dari file `__init__.py` ke file terpisah `views.py`.

## 2. Langkah Pengerjaan
1.  Menyalin proyek dari tutorial 06.
2.  Mengedit `tutorial/__init__.py`: menghapus *view function* lama, menambahkan rute baru (`/howdy`), dan menambahkan `config.scan('.views')`.
3.  Membuat file `tutorial/views.py`: memindahkan *view function* ke sini dan menghiasinya dengan `@view_config(route_name=...)`.
4.  Mengedit `tutorial/tests.py`: memperbarui *unit test* dan *functional test* untuk mencocokkan *views* dan *routes* yang baru.
5.  Menjalankan `pytest` (4 tes lolos) dan `pserve` untuk verifikasi di browser.

## 3. Hasil & Pembahasan
-   Keempat tes lolos (`....`).
-   Server berjalan dengan sukses.
-   URL `/` me-render *view* `home`.
-   URL `/howdy` me-render *view* `hello`.
-   Ini membuktikan bahwa pemisahan file berhasil.

## 4. Analisis Konsep Kunci
-   **`config.scan('.views')`**: Ini adalah perintah kuncinya. Ini memberitahu Pyramid, "Saat startup, tolong pindai file `views.py` (dan file lain di modul ini) dan cari *decorator* `@view_config`."
-   **`@view_config(route_name='home')`**: *Decorator* ini adalah "lem". Dia memberitahu Pyramid, "Fungsi `home()` ini harus dipanggil jika ada *request* yang cocok dengan rute yang bernama 'home'."
-   **Pemisahan (Separation of Concerns)**: Ini adalah praktik *software engineering* yang sangat baik.
    -   `__init__.py` sekarang hanya bertanggung jawab untuk *konfigurasi* dan *routing*.
    -   `views.py` sekarang bertanggung jawab untuk *logika bisnis* (apa yang harus dilakukan saat *request* masuk).
-   Kode menjadi jauh lebih bersih, rapi, dan mudah dikelola seiring bertambahnya jumlah *views*.

## 5. Kesimpulan
Saya belajar cara paling umum untuk mengatur *views* di Pyramid. Menggunakan `config.scan()` dan *decorator* `@view_config` jauh lebih rapi daripada mendaftarkan setiap *view* secara manual di `__init__.py`.