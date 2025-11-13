# Analisis 03: Application Configuration with .ini Files

## 1. Tujuan Percobaan
Mengubah aplikasi agar dijalankan menggunakan `pserve` dan file `.ini`, yang merupakan cara standar *deployment* Pyramid, dan tidak lagi bergantung pada `if __name__ == '__main__':`.

## 2. Langkah Pengerjaan
1.  Menyalin proyek dari tutorial 02.
2.  Menambahkan `entry_points` di `setup.py` yang menunjuk ke `tutorial:main`.
3.  Membuat file `development.ini` untuk mendefinisikan server (`waitress`) dan aplikasi (`egg:tutorial`).
4.  Memindahkan logika dari `app.py` ke `tutorial/__init__.py` dan membungkusnya dalam *app factory* bernama `main()`.
5.  Menghapus file `tutorial/app.py` yang sudah tidak terpakai.
6.  Menjalankan `pip install -e .` (untuk mendaftarkan entry point) dan `pserve development.ini --reload`.

## 3. Hasil & Pembahasan
-   Aplikasi berjalan sukses di `http://localhost:6543` sama seperti sebelumnya, tapi sekarang dijalankan oleh `pserve`.
-   Terminal menunjukkan log dari `pserve` dan `waitress`, bukan lagi output `print()` sederhana.

## 4. Analisis Kode & Perilaku
-   **`entry_points` di `setup.py`**: Ini adalah "iklan". Kita memberi tahu ekosistem Python, "Hei, jika ada yang mencari `paste.app_factory` bernama `main` untuk package `tutorial`, panggil fungsi `main` di dalam file `tutorial/__init__.py`."
-   **`development.ini`**: File ini menggunakan "iklan" tersebut. `use = egg:tutorial` pada dasarnya mencari *entry point* yang terdaftar untuk *package* `tutorial`.
-   **`def main(global_config, **settings)`**: Ini adalah *app factory*. `pserve` memanggil fungsi ini. Fungsi ini *mengembalikan* aplikasi WSGI yang sudah dikonfigurasi.
-   **`if __name__ == '__main__':` vs `pserve`**: Kita tidak lagi menjalankan file secara langsung. `pserve` adalah *runner* profesional yang tahu cara memuat aplikasi, membaca konfigurasi, dan menjalankan server (`waitress`) dengan benar.

## 5. Kesimpulan
Saya belajar cara mengonfigurasi dan menjalankan aplikasi Pyramid dengan cara yang "benar" menggunakan *entry points* dan `pserve`. Ini memisahkan konfigurasi server (`.ini`) dari logika aplikasi (`.py`).