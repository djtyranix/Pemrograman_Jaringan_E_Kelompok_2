# Tugas Kelompok Chat Application
## Pemrograman Jaringan - E
---
### Anggota Kelompok:
* Michael Ricky - 05111840000078
* Shofiyah Mardhiyah - 05111840000106
* Muhammad Satryo Pamungkas Bimasakti - 05111840000070

### Soal dan Pembagian Tugas:
* GUI untuk chat client - Shofiyah Mardhiyah
* Pengiriman dan penerimaan file antar user - Michael Ricky
* Group Chat - Muhammad Satryo Pamungkas Bimasakti

### Link Github:
* [Link to Github](https://github.com/djtyranix/Pemrograman_Jaringan_E_Kelompok_2/tree/TugasChat)

---

# Protokol
## 1. Client File

Client file dapat dijalankan dengan aturan protokol sebagai berikut:

* Program server telah berjalan pada server
* String dimasukkan dalam kolom input yang tersedia

GUI (Graphical User Interface) dibuat dalam suatu class bernama GUI. Class ini memiliki
beberapa method, yaitu:

* `__init__`

    Method inisialisasi kelas. Method ini akan memanggil beberapa method lainnya. Method ini
    juga akan menampilkan GUI login user. 

* `goAhead()`

    Method ini akan mengirimkan nama dan `room_id` ke server. Saat menerima respons, akan
    menampilkan halaman chat room.

* `layout()`

    Method ini adalah method yang digunakan untuk membuat keseluruhan GUI untuk chat room.

* `browseFile()`

    Method ini akan dipanggil ketika user ingin mencari file yang akan dikirim dalam
    chat room. Return dari method ini adalah lokasi file yang dipilih oleh client.

* `sendFile()`

    Method ini bertujuan untuk mengirim file yang direferensikan oleh lokasi yang
    dipilih client sebelumnya. Return dari method ini adalah nama file yang terkirim beserta
    pesan terkirim (jika terkirim) dan akan muncul pesan error jika ada error.

* `sendButton()`

    Method ini berfungsi untuk menghapus text yang ada pada kolom chat dan mengirim pesan yang telah dituliskan (baca: diketik) pada kolom chat melalui fungsi `sendMessage()`.

* `sendMessage()`

    Method ini akan dipanggil oleh `sendButton()` ketika client menekan tombol kirim. Method ini berfungsi untuk mengirim pesan dari kolom teks ke server, yang nantinya akan diteruskan ke seluruh peserta chat room yang sama.

* `receive()`

    Method ini bertujuan untuk menerima file dari server, menulis file pada client, dan memberikan notifikasi saat file diterima. Jika terjadi error pada penerimaan file maka server akan terputus.


## 2. Server File

Server file dapat dijalankan dengan aturan protokol sebagai berikut:

* Client mengirimkan request dalam bentuk **String**

File ini akan digunakan oleh server. Class server memiliki beberapa method, yaitu:

* `__init__`

    Method ini akan menginisialisasi kelas dan program.

* `accept_connections()`

    Method ini berfungsi untuk menginisiasi koneksi antara server dan client. Jika client berhasil terkoneksi, maka akan terbuat thread baru yang akan mengurusi respon dari suatu client tertentu. Jika gagal, maka koneksi akan terputus.

* `clientThread()`

    Method ini akan dijalankan dalam thread terpisah sebagai bentuk berhasilnya koneksi antara suatu client dan server. Jika suatu room belum dibuat, maka method ini akan membuat room dan mengembalikan pesan "Room berhasil dibuat". Jika suatu room sudah ada, maka method ini akan mengembalikan pesan "Selamat datang di Chat Room". Jika pesan yang diterima dari klien berbentuk string (text), maka akan memanggil method `broadcast()`, sementara jika pesan yang diterima adalah suatu file, maka akan memanggil method `broadcastFile()`. Jika gagal, maka koneksi akan terputus.

* `broadcastFile()`

    Method ini akan dipanggil ketika suatu client mengirimkan file ke dalam chat room. Return dari method ini adalah pesan terkirim dengan nama file yang dikirim. Jika gagal, maka koneksi akan terputus.

* `broadcast()`

    Method ini akan dipanggil ketika suatu client mengirimkan text ke dalam chat room. Return dari method ini adalah pesan terkirim dengan text yang dikirim. Jika gagal, maka koneksi akan terputus.

* `remove()`

    Method ini bertujuan untuk memutuskan koneksi antara suatu client dengan server.
