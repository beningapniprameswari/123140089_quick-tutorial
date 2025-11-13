# Analisis 02: Python Packages for Pyramid Applications

## 1. Tujuan Percobaan
Tujuan dari tutorial ini adalah untuk mengubah struktur proyek dari satu file .py tunggal menjadi sebuah *package* Python yang dapat didistribusikan dan diinstal.

## 2. Langkah Pengerjaan
1.  Membuat folder `02-Python-Packages`.
2.  Membuat file `setup.py` untuk mendefinisikan *package* kita (bernama 'tutorial') dan dependensinya (`pyramid`, `waitress`).
3.  Membuat folder `tutorial/` yang berisi kode aplikasi.
4.  Membuat `tutorial/__init__.py` (meskipun kosong) untuk menandai folder `tutorial/` sebagai *package* Python.
5.  Memindahkan kode `app.py` dari tutorial 01 ke dalam `tutorial/app.py`.
6.  Menjalankan `pip install -e .` dari dalam folder `02-Python-Packages` untuk menginstal *package* kita.
7.  Menjalankan `python tutorial/app.py` untuk menyalakan server.

## 3. Hasil & Pembahasan
-   Aplikasi berjalan dengan sukses di `http://localhost:6543`.
-   Hasilnya di browser **tidak ada bedanya** dengan Tutorial 01.

## 4. Analisis Kode & Perilaku
-   **`setup.py`**: Ini adalah file konfigurasi untuk `setuptools`. `install_requires` memberi tahu `pip` apa saja yang perlu diinstal bersama *package* ini.
-   **`pip install -e .`**: Perintah ini sangat penting. `-e` berarti *editable*. Ini membuat *link* ke kode kita alih-alih menyalinnya. Jadi, jika kita mengubah kode di `tutorial/app.py`, perubahannya akan langsung terlihat tanpa perlu instal ulang.
-   **Perilaku yang Sama**: Alasan utama hasilnya sama adalah karena kita masih menjalankan aplikasi dengan cara yang sama: `python tutorial/app.py`. Kita mengeksekusi file tersebut secara langsung, dan blok `if __name__ == '__main__':` di dalamnya masih berjalan seperti biasa.

Saat ini, kita **belum benar-benar memanfaatkan** fakta bahwa ini adalah *package*. Kita hanya mengubah strukturnya. Tutorial selanjutnya (kemungkinan besar) akan menunjukkan cara menjalankan aplikasi *sebagai package* (menggunakan `pserve` dan `.ini`), yang tidak lagi bergantung pada blok `if __name__ == '__main__':`.

## 5. Kesimpulan
Saya belajar cara mengemas aplikasi Pyramid ke dalam struktur *package* Python standar menggunakan `setup.py`. Ini adalah langkah pertama untuk membuat aplikasi yang lebih terstruktur dan siap untuk *deployment*.