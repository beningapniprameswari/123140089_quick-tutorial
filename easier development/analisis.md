# Analisis 04: Easier Development with debugtoolbar

## 1. Tujuan Percobaan
Menginstal dan mengaktifkan `pyramid_debugtoolbar`, sebuah add-on yang sangat berguna untuk debugging aplikasi Pyramid selama masa pengembangan.

## 2. Langkah Pengerjaan
1.  Menyalin proyek dari tutorial 03.
2.  Memodifikasi `setup.py` untuk menambahkan `pyramid_debugtoolbar` di bawah `extras_require={'dev': ...}`.
3.  Memodifikasi `development.ini` untuk menambahkan `pyramid.includes = pyramid_debugtoolbar`.
4.  Menjalankan `pip install -e ".[dev]"` untuk menginstal dependensi *development*.
5.  Menjalankan `pserve development.ini --reload`.

## 3. Hasil & Pembahasan
-   Aplikasi berjalan seperti biasa, tetapi sekarang muncul *toolbar* melayang di sisi kanan browser.
-   Ketika diklik, *toolbar* ini membuka panel *debug* yang sangat lengkap.
-   Fitur yang paling berguna adalah:
    * **Request Vars**: Menampilkan data GET, POST, dan URL.
    * **Settings**: Menampilkan semua konfigurasi yang dimuat dari `.ini`.
    * **Routes**: Menampilkan semua rute (URL) yang terdaftar di aplikasi.
    * **SQLAlchemy**: (Akan berguna nanti) Menampilkan *query database* yang dijalankan.

## 4. Analisis Kode
-   **`extras_require={'dev': ...}`**: Ini adalah cara *best practice* untuk mengelola dependensi. `pytest` dan `debugtoolbar` adalah alat bantu *development*, bukan bagian inti dari aplikasi. Dengan cara ini, kita bisa menginstal aplikasi di *production* tanpa alat-alat *debug* ini.
-   **`pyramid.includes = ...`**: Ini adalah cara Pyramid untuk mengaktifkan *add-on*. Saat *startup*, Pyramid akan membaca baris ini dan memuat konfigurasi dari *package* `pyramid_debugtoolbar`.

## 5. Kesimpulan
`pyramid_debugtoolbar` adalah alat bantu *debugging* yang wajib dipakai. Mengaktifkannya sangat mudah (hanya 2 file) dan manfaatnya sangat besar untuk melihat "apa yang sebenarnya terjadi" di dalam aplikasi.