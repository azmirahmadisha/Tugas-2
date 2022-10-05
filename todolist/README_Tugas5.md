Aplikasi Heroku dapat diakses pada [tautan berikut](http://katalog-tugas2.herokuapp.com/todolist/).
<br />

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman. Sementara Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.

<br />

### Jelaskan tag HTML5 yang kamu ketahui.

Beberapa tag HTML5 antara lain:
  1. "<a>" yang digunakan untuk mendefinisikan sebuah hyperlink / meletakkan tautan.
  2. "<b>" yang digunakan untuk menampilkan text dalam gaya bold/huruf tebal.
  3. "<br>" yang digunakan untuk memberi break single line.
  4. "<button>" yang membuat sebuah tombol di HTML.
  5. "<div>" yang menspesifikasikan sebuah section dalam dokumen/file HTML.
  6. "<li>" yang mendefinisikan sebuah item list.
  6. "<p>" yang berarti paragraf.

<br />

###  Jelaskan tipe-tipe CSS selector yang kamu ketahui.

  Beberapa tipe CSS selector antara lain:
  1. id Selector, yaitu sebuah selector yang menggunakan atribut id dari sebuah elemen HTML untuk memilih sebuah elemen yang spesifik. Id selector ditandai dengan tanda pagar (#).
  2. class Selector, yaitu sebuah selector yang memilih elemen HTML dengan sebuah atribut kelas yang spesifik. Class selector ditandai dengan titik sebelum namanya.
  3. Universal Selector, yaitu selector yang memilih semua elemen di berkas HTML. Selector ini ditandai dengan tanda bintang.
  4. Grouping Selector, yaitu selector yang memilih semua elemen HTML dengan definisi style yang sama. Misal: h1, h3, h5.

 ### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. <p align="justify">Poin pertama dilakukan dengan menjalankan perintah python manage.py startapp todolist pada Command Prompt. Perintah ini akan secara otomatis membuat sebuah aplikasi dalam bentuk folder, beserta beberapa file bawaan python yang digunakan untuk menyokong aplikasi yang telah dibuat (pada kasus ini, aplikasi bernama todolist). </p>
2. <p align="justify">Poin kedua dilakukan dengan membuat sebuah file bernama urls.py di dalam folder aplikasi todolist dan melakukan routing agar aplikasi todolist dapat diakses melalui browser. Path dari aplikasi todolist dimasukkan ke sebuah variable bernama urlpatterns. Selanjutnya, proses dilanjutkan dengan menambahkan url 'todolist.html' di file urls.py yang terletak di dalam folder project_django. </p>
3. <p align="justify"> Poin ketiga dilakukan dengan mengisi file models.py yang terletak di dalam folder aplikasi todolist dengan cara membuat class bernama Task yang memiliki variable-variable yang diminta, yaitu user (menggunakan tipe model ForeignKey dengan parameter User), date, title, dan description. Setiap variable yang dibuat memiliki tipe data yang disesuaikan dengan kebutuhan aplikasi.  </p>
4. <p align="justify"> Pada poin keempat, yang pertama dilakukan adalah membuat form registrasi. Proses ini dilakukan dengan membuat sebuah fungsi register pada views.py yang menerima parameter request. Tambahkan juga import redirect, UserCreationForm, dan messages pada bagian paling atas views.py. Kemudian, fungsi register diisi dengan perintah yang sesuai.</p>

5. <p align="justify">Poin kelima dilakukan dengan membuat sebuah berkas HTML dengan nama todolist.html di dalam folder templates. Berkas HTML secara umum berisi judul halaman, username dari user yang sedang log in, lalu melakukan iterasi untuk setiap elemen yang ada pada model Task. Field-field tersebut akan ditampilkan dalam bentuk tabel sehingga digunakan tag table. Selanjutnya, ditambahkan tombol tambah task baru yang nantinya akan dikaitkan dengan fungsi pembuatan task. </p>
 
6. <p align="justify">Poin keenam dilakukan dengan membuat sebuah fungsi dengan nama create_task di views.py. Fungsi ini akan menerima parameter request dan mengembalikan redirect ke halaman html bernama create-task. Fungsi ini melakukan pengambilan dan penyimpanan data yang dimasukkan oleh user sebagai input. Kemudian, dibuat sebuah berkas HTML yang secara garis besar berisi form untuk meminta nama dan deskripsi dari tag. Selanjutnya, dilakukan routing url dengan mengimpor fungsi create_Task di berkas urls.py yang ada di folder todolist dan menambahkan path ke variable urlpatterns.</p>
  
7. <p align="justify">Routing halaman telah dilakukan pada langkah sebelumnya, yaitu dengan mengimport fungsi yang diinginkan, lalu menambahkan path fungsi tersebut ke variable urlpatterns.</p>
  
8. <p align="justify">Deployment ke Heroku dilakukan dengan membuat sebuah aplikasi di laman Heroku dan membuat repository secrets berisi nama aplikasi Heroku dan API key dari aplikasi Heroku. Setelah itu, workflow yang tadinya gagal akan dijalankan kembali dan deployment selesai. </p>
  
9. <p align="justify">Poin terakhir dilakukan dengan membuat akun langsung setelah dapat mengakses web dari aplikasi Heroku, lalu menambahkan task pada masing-masing akun yang telah dibuat. </p>
  

<br />
