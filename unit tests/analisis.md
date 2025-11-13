# Analisis 05: Unit Tests and pytest

## 1. Tujuan Percobaan
Memperkenalkan *unit testing* ke dalam proyek. Tujuannya adalah menulis kode (tes) yang memverifikasi bahwa satu "unit" kode (fungsi `hello_world`) bekerja seperti yang diharapkan.

## 2. Langkah Pengerjaan
1.  Menyalin proyek dari tutorial 04.
2.  Menambahkan `pytest` ke `dev_requires` di `setup.py`.
3.  Menjalankan `pip install -e ".[dev]"` untuk menginstal `pytest`.
4.  Membuat file `tutorial/tests.py` yang berisi *test case* baru.
5.  Menjalankan tes menggunakan perintah `pytest`.

## 3. Hasil & Pembahasan
-   Perintah `pytest tutorial/tests.py -q` berhasil dijalankan.
-   Outputnya adalah `. 1 passed ...`, yang menunjukkan bahwa satu tes (`test_hello_world`) ditemukan dan berhasil dijalankan.

## 4. Analisis Kode Tes
Ini adalah bagian terpenting. Kita **tidak menjalankan server web** sama sekali.
-   **`pyramid.testing`**: *Library* ini sangat penting. `testing.setUp()` membuat konfigurasi Pyramid *tiruan* (mock) yang minimalis.
-   **`testing.DummyRequest()`**: Kita tidak perlu browser untuk mengirim *request*. Kita membuat objek *request* tiruan di dalam kode.
-   **`response = hello_world(request)`**: Kita memanggil *view function* kita (`hello_world`) secara langsung, persis seperti memanggil fungsi Python biasa.
-   **`self.assertEqual(response.status_code, 200)`**: Ini adalah *assertion*. Kita menguji apakah *response* yang dikembalikan oleh fungsi memiliki `status_code` 200 (OK). Jika tidak, tes akan gagal.

## 5. Kesimpulan
Saya belajar cara melakukan *unit test* pada *view* Pyramid. Kuncinya adalah menguji fungsi *view* secara terisolasi (sebagai fungsi Python biasa) dan menggunakan `pyramid.testing` untuk "menipu" fungsi tersebut agar seolah-olah berjalan di dalam aplikasi Pyramid.