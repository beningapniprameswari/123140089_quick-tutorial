# Analisis 06: Functional Testing with WebTest

## 1. Tujuan Percobaan
Memperkenalkan *functional testing* menggunakan `WebTest`. Berbeda dengan *unit test* yang menguji fungsi secara terisolasi, *functional test* menguji seluruh *stack* aplikasi, termasuk *routing* dan *request handling*, seolah-olah ada browser yang mengaksesnya.

## 2. Langkah Pengerjaan
1.  Menyalin proyek dari tutorial 05.
2.  Menambahkan `webtest` ke `dev_requires` di `setup.py`.
3.  Menjalankan `pip install -e ".[dev]"` untuk menginstal `webtest`.
4.  Memodifikasi `tutorial/tests.py` dengan menambahkan *class* baru `TutorialFunctionalTests`.
5.  Menjalankan `pytest` dan memverifikasi bahwa 2 tes berhasil.

## 3. Hasil & Pembahasan
-   Perintah `pytest` berhasil menemukan dan menjalankan kedua *test class* (total 2 tes).
-   Outputnya adalah `.. 2 passed ...`.

## 4. Perbedaan Kunci: Unit Test vs Functional Test

Ini adalah analisis terpenting dari tutorial ini:

| Fitur | Unit Test (Tutorial 05) | Functional Test (Tutorial 06) |
| :--- | :--- | :--- |
| **Apa yang dites?** | Satu fungsi (`hello_world`) secara terisolasi. | Seluruh *stack* aplikasi (routing, view, response). |
| **Request** | `testing.DummyRequest()` (Request palsu). | `self.testapp.get('/')` (Mensimulasikan HTTP GET asli). |
| **Setup** | `testing.setUp()` (Membuat config Pyramid palsu). | `app = main({})` (Memuat *seluruh aplikasi* yang sebenarnya). |
| **Verifikasi** | `response.status_code` (Mengecek properti objek). | `res.body` (Mengecek *isi HTML* dari *response*). |
| **Analogi** | Menguji apakah mesin mobil menyala. | Menguji apakah mobil bisa dikendarai mengelilingi blok. |

**Analisis Kode `TutorialFunctionalTests`:**
-   `from tutorial import main; app = main({})`: Kita mengimpor dan menjalankan *app factory* (`main`) kita yang sebenarnya.
-   `self.testapp = TestApp(app)`: `WebTest` "membungkus" aplikasi kita, memberinya *interface* untuk dites.
-   `res = self.testapp.get('/', status=200)`: Ini adalah perintah kuncinya. `WebTest` melakukan request `GET` ke path `/`, lalu mengecek apakah *status code*-nya 200. Ini **menguji sistem routing** kita.
-   `self.assertIn(b'<h1>Hello World!</h1>', res.body)`: Kita mengecek apakah `res.body` (HTML yang dikembalikan) berisi *string bytes* `b'<h1>...`.`

## 5. Kesimpulan
Saya belajar bahwa *functional test* memberikan keyakinan lebih tinggi bahwa aplikasi bekerja *end-to-end*. *Unit test* baik untuk logika, *functional test* baik untuk alur kerja.