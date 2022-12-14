Aplikasi Heroku dapat diakses pada [tautan berikut](http://katalog-tugas2.herokuapp.com/todolist/).
<br />

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
<p align="justify">Asynchronous Programming adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Sementara itu, Synchronous Programming adalah proses jalannya program secara sequential (berdasarkan antrian eksekusi program).  Synchronous merupakan bagian dari Asynchronous (1 antrian) dimana proses akan dieksekusi secara bersamaan dan untuk hasil tergantung lama proses suatu fungsi synchronous. </p>


### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
<p align="justify">Event-driven programming adalah paradigma pemrograman di mana aliran program ditentukan oleh peristiwa seperti tindakan pengguna (klik mouse, penekanan tombol), keluaran sensor, atau pesan yang lewat dari program atau utas lain. Event-driven programming digunakan untuk menyinkronkan terjadinya beberapa peristiwa dan membuat program sesederhana mungkin. Contoh dari penerapannya pada tugas ini adalah tombol Add Task pada halaman ‘todolist/’ yang akan mengantarkan pengguna ke modal form pembuatan task ketika ditekan.</p>


### Jelaskan penerapan asynchronous programming pada AJAX.
<p align="justify">Di AJAX, setelah halaman HTML dimuat, data dibaca dari server web. Tanpa perlu memuat ulang halaman web, data dapat diperbarui. Transfer data terjadi ke server web di belakang layar. AJAX dapat berkomunikasi dengan server, bertukar data, dan memperbarui halaman tanpa harus me-refresh halaman. Secara garis besar, AJAX memungkinkan pengguna untuk membuat permintaan ke server tanpa memuat ulang halaman.</p>


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. <p align="justify">Menambahkan fungsi ‘show_json’ pada views.py yang me-return HttpResponse dengan bantuan serializers untuk menampilkan data JSON. </p>
2. <p align="justify">Menambahkan fungsi ‘add_todolist_ajax’ pada views.py untuk membuat task baru. Lalu, membuat path ‘/todolist/add’ yang tersambung dengan fungsi tersebut.</p>
3. <p align="justify">Membuat sebuah path ‘/todolist/json’ yang akan memanggil fungsi show_json untuk menampilkan data JSON di HTML.</p>
4. <p align="justify">Membuat fungsi asinkron Script getTodoList di todolist.html yang melakukan fetching data dari fungsi show_json yang telah dibuat di views. </p>
5. <p align="justify">Membuat fungsi asinkron Script refreshTodolist() untuk menampilkan data yang sudah di-fetch dari JSON. </p>
6. <p align="justify">Membuat button Add Task yang akan mengarahkan ke modal form pembuatan Task.</p>
7. <p align="justify">Membuat modal berisi form pembuatan task yang memiliki close button. </p>
8. <p align="justify">Membuat fungsi asinkron Script addTodolist yang terhubung dengan fungsi add_todolist_ajax yang sudah dibuat di views.py. Fungsi ini akan memanggil fungsi refreshTodolist() pada line akhir untuk melakukan refresh setelah penambahan task baru.</p>
	

