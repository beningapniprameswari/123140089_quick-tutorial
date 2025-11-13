# Analisis 08: HTML Generation With Templating

## 1. Tujuan Percobaan
Memisahkan *logic* (Python) dari *presentation* (HTML) dengan menggunakan *template engine* `pyramid_chameleon`. Ini adalah praktik fundamental dalam pengembangan web.

## 2. Langkah Pengerjaan
1.  Menyalin proyek dari tutorial 07.
2.  Menambahkan `pyramid_chameleon` ke `setup.py` dan menginstalnya via `pip install -e .`.
3.  Mengaktifkan *add-on* di `__init__.py` dengan `config.include('pyramid_chameleon')`.
4.  Membuat file template `tutorial/home.pt` yang berisi HTML dan *placeholder* `${name}`.
5.  Mengubah `views.py`: mengganti `renderer` di `@view_config` dan mengubah *return value* dari `Response` menjadi `dict`.
6.  Menambahkan `pyramid.reload_templates = true` di `.ini` untuk kenyamanan development.
7.  Memperbarui *unit test* untuk mengecek *dictionary* dan *functional test* untuk mengecek HTML yang sudah di-render.

## 3. Hasil & Pembahasan
-   Keempat tes lolos.
-   Browser berhasil me-render HTML dari file `.pt`. Data (`'Home View'` atau `'Hello View'`) berhasil disisipkan ke dalam *placeholder* `${name}`.
-   Perubahan pada file `home.pt` langsung terlihat di browser setelah di-refresh (tanpa restart server) berkat `reload_templates`.

## 4. Analisis Konsep Kunci: Renderer
Konsep paling penting di sini adalah **`renderer`** di `@view_config`.

`@view_config(route_name='home', renderer='home.pt')`

Ini memberi tahu Pyramid untuk melakukan hal berikut:
1.  **JANGAN** kirimkan *return value* dari fungsi `home()` (yaitu `dict`) langsung ke browser.
2.  **SEBALIKNYA**, ambil *dictionary* itu: `{'name': 'Home View'}`.
3.  Cari file template yang bernama `home.pt`.
4.  Jalankan *template engine* (Chameleon) untuk "mengisi" file `home.pt` dengan data dari *dictionary*. (Mengganti `${name}` dengan `Home View`).
5.  Ambil hasil HTML-nya dan kirimkan sebagai `Response` ke browser.

**Perubahan pada Tes:**
-   **Unit Test** (`TutorialViewTests`): Menguji "apa yang dilakukan *fungsi*?". Fungsi `home()` sekarang *hanya* mengembalikan `dict`. Jadi, unit test-nya mengecek isi `dict` tersebut.
-   **Functional Test** (`TutorialFunctionalTests`): Menguji "apa yang dilihat *browser*?". Browser melihat hasil akhir *setelah* *renderer* bekerja. Jadi, *functional test* mengecek HTML yang sudah di-render.

## 5. Kesimpulan
Memisahkan logika (views.py) dari presentasi (home.pt) membuat kode SANGAT lebih bersih. *View* saya sekarang fokus pada *data*, dan *template* saya fokus pada *tampilan*.