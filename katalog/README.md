Aplikasi Heroku dapat diakses pada [tautan berikut](http://katalog-tugas2.herokuapp.com/katalog/).
<br />

#### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;


![Image](/katalog/Flowchart.png)

<p align="justify"> Berdasarkan bagan di atas, URL Mapper (urls.py) digunakan untuk mengarahkan permintaan HTTP dari client ke view yang sesuai berdasarkan URL yang di-request. URL Mapper (urls.py) juga kemudian dapaet mencocokkan pola string atau angka tertentu yang muncul di URL dan meneruskannya ke fungsi tampilan sebagai data. Selanjutnya, pada bagian selanjutnya, View (views.py) akan mengakses data yang dibutuhkan untuk memenuhi request client melalui models dan menyerahkan formatting dari respons ke template. Sementara itu, model berperan sebagai penyedia mekanisme untuk mengelola dan meminta catatan di database, serta mendefinisikan struktur dari data aplikasi. Template sendiri berperan untuk mendefinisikan struktur file (misal: halaman HTML). Dalam hubungannya dengan view, sebagai contoh, file views.py dapat membuat sebuah halaman HTML dengan memanfaatkan template HTML dan mengisinya dengan data yang didapat dari file model. </p>

<br />

#### Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

<p align="justify"> Sebenernya kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi
penggunaan virtual environment dalam pengembangan aplikasi web berbasis Django mengantisipasi modul-modul yang ada
menjadi tumpang tindih. Hal ini dilakukan agar instalasi-instalasi yang kita lakukan pada proyek Django tersebut
menjadi terisolasi. Penggunaan virtual environment juga memungkinkan versi proyek Django tetap konsisten meskipun
pengguna menggunakan device yang berbeda. </p>


<br />

#### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

1. <p align="justify">Poin pertama dilakukan dengan membuat file views.py yang melakukan import CatalogItem dari models.py yang sudah tersedia. Pada file views.py, dibuat sebuah fungsi yang menerima parameter request dan melakukan rendering ke file html. </p>

2. <p align="justify">Poin kedua dilakukan dengan mengimport fungsi show_katalog yang ada pada file views.py. Selaunjutnya, fungsi show_wishlist didaftarkan pada urlpatterns. Aplikasi katalog juga kemudian ditambahkan pada variable urlpatterns di file urls.py yang ada di folder project_django dengan command path include. </p>

3. <p align="justify">Pemetaan data untuk ditampilkan ke katalog.html dilakukan dengan menggunakan variable-variable yang sudah dibuat pada fungsi show_katalog di file views.py. Data barang di-load dengan melakukan iterasi untuk setiap elemen di variable list_item agar dapat ditampilkan di halaman HTML. Untuk melihat halaman HTML sebelum di-deploy, digunakan command runserver untuk dapat mengakses localhost:8000. </p>

4. <p align="justify">Deployment ke Heroku dilakukan dengan membuat sebuah aplikasi di laman Heroku dan membuat repository secrets berisi nama aplikasi Heroku dan API key dari aplikasi Heroku. Setelah itu, workflow yang tadinya gagal akan dijalankan kembali dan deployment selesai. </p>
