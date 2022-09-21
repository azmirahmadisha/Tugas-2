Aplikasi Heroku dapat diakses pada [tautan berikut](http://katalog-tugas2.herokuapp.com/mywatchlist/).
<br />

### Jelaskan perbedaan antara JSON, XML, dan HTML!

<p align="justify">JSON (JavaScript Object Notation) adalah sebuah format data yang digunakan untuk pertukaran dan penyimpanan data. JSON digunakan untuk menyimpan informasi dengan cara yang terorganisir dan mudah diakses. Bentuk lengkapnya adalah JavaScript Object Notation. JSON menawarkan kumpulan data yang dapat dibaca manusia yang dapat diakses secara logis. XML adalah bahasa markup yang dirancang untuk menyimpan data. XML populer digunakan untuk melakukan transfer data. Sementara itu, HTML adalah bahasa standar pemrogaman yang digunakan untuk membuat halaman website, yang diakses melalui internet.</p>

<p align="justify">Meskipun JSON dan XML sama-sama merupakan return result dari HTTP request ketika browser me-request data, JSON dan XML/HTML sendiri sudah memiliki perbedaan yang signifikan karena JSON adalah sebuah format pertukaran data sementara XML dan HTML adalah bahasa markup yang digunakan untuk mengekspresikan dan menyusun konten. Ketika JSON merupakan sebuah cara untuk merepresentasikan data, XML adalah sebuah markup language yang menggunakan struktur tag untuk merepresentasikan item data. JSON digunakan untuk merepresentasikan data sebagai pasangan nilai kunci, yang dapat dengan mudah dikonversi ke dan dari objek JavaScript.

Di sisi lain, perbedaan HTML dan XML adalah HTML menitikberatkan pada bagaimana format tampilan dari data, sedangkan XML menitikberatkan pada struktur dan konteksnya. Ketika HTML memiliki data dan representasinya, XML hanya memiliki data. HTML digunakan untuk menyusun teks pada halaman web agar ditampilkan dengan tepat di browser web, sementara XML umumnya digunakan untuk menyusun data atau pesan.</p>

<br />

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

<p align="justify"> Data delivery digunakan untuk melakukan transfer data dari suatu format ke format yang lain. Dalam mengimplementasikan sebuah platform, mekanisme data delivery dibutuhkan untuk menyajikan data sesuai dengan request yang diterima dari client. Sebagai contoh, ketika client melakukan request halaman HTML page, server akan mengembalikan berkas dalam format HTML. Begitu pula ketika client melakukan request data, format yang akan dikembalikan adalah JSOn atau XML. Proses-proses di atas tidak akan dapat dilakukan jika kita tidak melakukan data delivery.  </p>


<br />

### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

1. <p align="justify">Poin pertama dilakukan dengan menjalankan perintah python manage.py startapp mywatchlist pada Command Prompt. Perintah ini akan secara otomatis membuat sebuah aplikasi dalam bentuk folder, beserta beberapa file bawaan python yang digunakan untuk menyokong aplikasi yang telah dibuat (pada kasus ini, aplikasi bernama mywatchlist). </p>
2. <p align="justify">Poin kedua dilakukan dengan membuat sebuah file bernama urls.py di dalam folder aplikasi mywatchlist dan melakukan routing agar aplikasi mywatchlist dapat diakses melalui browser. Path dari aplikasi mywatchlist dimasukkan ke sebuah variable bernama urlpatterns. Selanjutnya, proses dilanjutkan dengan menambahkan url 'mywatchlist.html' di file urls.py yang terletak di dalam folder project_django. </p>
3. <p align="justify"> Poin ketiga dilakukan dengan mengisi file models.py yang terletak di dalam folder aplikasi mywatchlist dengan cara menambahkan variable-variable yang diminta, yaitu watched, title, rating, release date, dan reviews. Setiap variable yang dibuat memiliki tipe data yang disesuaikan dengan kebutuhan aplikasi.  </p>
4. <p align="justify"> Poin keempat dilakukan dengan membuat sebuah folder baru bernama fixtures di dalam folder aplikasi mywatchlist, lalu membuat file JSON yang berisi 10 data dari film yang dimasukkan ke dalam watchlist. Pengisian data dilakukan dengan berpatokan pada tipe data yang telah diatur di file models.py sebelumnya. </p>
5. <p align="justify"> Poin kelima dilakukan dengan menambahkan line import HttpResponse dan serializers di file views.py, lalu membuat dua fungsi bernama show_xml dan show_json untuk melakukan rendering aplikasi dalam format xml dan json. Di dalam kedua fungsi, dibuat sebuah variable bernama data yang menyimpan hasil query dari seluruh data yang ada di WatchlistItem pada file models.py. Fungsi tersebut akan melakukan return function HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML/JSON dan parameter content_type="application/xml" atau content_type="application/json" sesuai dengan fungsinya. </p>
6. <p align="justify"> Poin keenam dilakukan dengan menambahkan line import fungsi show_xml dan show_json di file urls.py yang ada di dalam folder aplikasi mywatchlist. Selanjutnya, proses dilanjutkan dengan menambahkan path url ke dalam urlpatterns agar fungsi yang sudah diimpor dapat diakses. </p>
7. <p align="justify">Deployment ke Heroku dilakukan dengan membuat sebuah aplikasi di laman Heroku dan membuat repository secrets berisi nama aplikasi Heroku dan API key dari aplikasi Heroku. Setelah itu, workflow yang tadinya gagal akan dijalankan kembali dan deployment selesai. </p>

<br />

### Mengakses tiga URL di poin 6 menggunakan Postman, menangkap screenshot, dan menambahkannya ke dalam README.md
1. http://127.0.0.1:8000/mywatchlist/html/
![Image](/mywatchlist/postman-html.png)

2. http://127.0.0.1:8000/mywatchlist/json/
![Image](/mywatchlist/postman-json.png)

3. http://127.0.0.1:8000/mywatchlist/xml/
![Image](/mywatchlist/postman-xml.png)

