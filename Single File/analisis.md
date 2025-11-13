# Analisis 01: Single-File Web Applications

## 1. Tujuan Percobaan
Tujuan dari tutorial ini adalah untuk membuat dan menjalankan aplikasi web Pyramid yang paling sederhana, hanya menggunakan satu file Python, dan menjalankannya dengan server WSGI `waitress`.

## 2. Langkah Pengerjaan
1.  Membuat file `app.py`.
2.  Menginstal dependensi (`pyramid` dan `waitress`) menggunakan `pip`.
3.  Menjalankan aplikasi langsung dengan `python app.py`.
4.  Mengakses `http://localhost:6543` di browser.

## 3. Hasil & Pembahasan
-   Browser berhasil menampilkan `<h1>Hello World!</h1>`.
-   Terminal tempat `python app.py` dijalankan mencetak log "Incoming request" setiap kali halaman di-refresh.

## 4. Analisis Kode
-   **`from waitress import serve`**: Mengimpor server `waitress` yang akan menjalankan aplikasi kita.
-   **`def hello_world(request):`**: Ini adalah *view callable*. Fungsi ini menerima objek `request` dan harus mengembalikan objek `Response`.
-   **`print('Incoming request