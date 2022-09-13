Aplikasi Heroku dapat diakses pada [tautan berikut](http://katalog-tugas2.herokuapp.com/katalog/).


#### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;




#### Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Sebenernya kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi
penggunaan virtual environment dalam pengembangan aplikasi web berbasis Django mengantisipasi modul-modul yang ada
menjadi tumpang tindih. Hal ini dilakukan agar instalasi-instalasi yang kita lakukan pada proyek Django tersebut
menjadi terisolasi. Penggunaan virtual environment juga memungkinkan versi proyek Django tetap konsisten meskipun
pengguna menggunakan device yang berbeda.



#### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

1. Poin pertama dilakukan dengan membuat file views.py yang melakukan import CatalogItem dari models.py yang sudah 
tersedia. Pada file views.py, dibuat sebuah fungsi yang menerima parameter request dan melakukan rendering ke file
html.

2. Poin kedua dilakukan dengan mengimport fungsi show_katalog yang ada pada file views.py. Selaunjutnya, fungsi show_wishlist didaftarkan
pada urlpatterns. Aplikasi katalog juga kemudian ditambahkan pada variable urlpatterns di file urls.py yang ada
di folder project_django dengan command path include.

3. Pemetaan data untuk ditampilkan ke katalog.html dilakukan dengan menggunakan variable-variable yang sudah dibuat pada fungsi show_katalog
di file views.py. Data barang di-load dengan melakukan iterasi untuk setiap elemen di variable list_item.

4. Deployment ke Heroku dilakukan dengan membuat repository secrets berisi nama aplikasi Heroku dan API key dari aplikasi Heroku. Setelah itu,
workflow yang tadinya gagal akan dijalankan kembali dan deployment selesai.
