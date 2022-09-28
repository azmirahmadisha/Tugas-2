Aplikasi Heroku dapat diakses pada [tautan berikut](http://katalog-tugas2.herokuapp.com/todolist/).
<br />

### Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

<p align="justify">Django memiliki tag {% csrf_token %} yang diimplementasikan untuk menghindari serangan berbahaya. Ini menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi.</p>
  
<p align="justify">Token CSRF sendiri adalah token acak aman yang digunakan untuk mencegah serangan CSRF. Token harus unik per sesi pengguna dan harus bernilai acak besar agar sulit ditebak. Aplikasi aman CSRF memberikan token CSRF unik untuk setiap sesi pengguna.</p>
  
<p align="justiyf">Ketika kita tidak menggunakan tag tersebut, kita tidak dapat menghindari serangan yang dapat muncul dan tidak dapat memastikan keamanan request post dari pengguna ke server.</p>

<br />

### Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

<p align="justify">Ya, kita dapat membuat elemen form tanpa menggunakan generator seperti {{form.as_table}} attau {{form}} dengan memanfaatkan template engine. Yang harus dilakukan adalah membuat sebuah file dengan nama forms.py di mana kita akan menggunakan class Form. Dalam class tersebut, akan ditulis variabel-variabel yang akan diminta pada form. 
Kemudian, untuk melakukan rendering form tersebut ke view, akan dibuat sebuah fungsi yang menerima parameter request dan melakukan rendering ke HTML. Pada fungsi tersebut, akan dibuat sebuah instance dari kelas Form yang telah dibuat di forms.py. Selanjutnya, untuk melakukan penyesuaian, dimanfaatkan atribut {{ field }} sehingga jika kita memiliki atribut nama dan lokasi, yang akan ditulis pada potongan kode HTML adalah:</p>

```
  <form action='' method=''>
   {% csrf_token %}
   {{ form.name}}
   {{form.locaiton}}
   <input type='submit' />
</form>
```

<br />

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
<p align="justify"Pertama, browser akan me-generate HTTP request ke alamat path yang dituju setelah user mengetik alamat path yang ingin diakses pada browser yang digunakan. Browser akan menerima HTTP request dari browser, kemudian menentukan views.py yang akan meng-handle request tersebut sebelum men-generate halaman HTML dari form yang ingin diakses user. Browser kemudian akan menampilkan halaman HTML ke user dan user akan mulai mengisi form. Browser kemudian akan men-generate HTTP request, metode, dan argumen ke URL tujuan
berdasarkan halaman HTML form. Server akan menerima HTTP request dari bwoser, lalu menentukan views.py mana yang akan meng-handle request tersebut. Pada tahap ini, data yang didapatkan dari input user akan disimpan dalam database sebelum kemudian server akan men-generate halaman HTML. Browser kemudian akan menampilan halaman tersebut kepada user. </p>

 ### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. <p align="justify">Poin pertama dilakukan dengan menjalankan perintah python manage.py startapp todolist pada Command Prompt. Perintah ini akan secara otomatis membuat sebuah aplikasi dalam bentuk folder, beserta beberapa file bawaan python yang digunakan untuk menyokong aplikasi yang telah dibuat (pada kasus ini, aplikasi bernama todolist). </p>
2. <p align="justify">Poin kedua dilakukan dengan membuat sebuah file bernama urls.py di dalam folder aplikasi todolist dan melakukan routing agar aplikasi todolist dapat diakses melalui browser. Path dari aplikasi todolist dimasukkan ke sebuah variable bernama urlpatterns. Selanjutnya, proses dilanjutkan dengan menambahkan url 'todolist.html' di file urls.py yang terletak di dalam folder project_django. </p>
3. <p align="justify"> Poin ketiga dilakukan dengan mengisi file models.py yang terletak di dalam folder aplikasi todolist dengan cara membuat class bernama Task yang memiliki variable-variable yang diminta, yaitu user (menggunakan tipe model ForeignKey dengan parameter User), date, title, dan description. Setiap variable yang dibuat memiliki tipe data yang disesuaikan dengan kebutuhan aplikasi.  </p>
4. <p align="justify"> Pada poin keempat, yang pertama dilakukan adalah membuat form registrasi. Proses ini dilakukan dengan membuat sebuah fungsi register pada views.py yang menerima parameter request. Tambahkan juga import redirect, UserCreationForm, dan messages pada bagian paling atas views.py. Kemudian, fungsi register diisi dengan perintah yang sesuai.</p>
  
```
  def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)
  ```
  
    Setelah itu, akan dibuat sebuah berkas HTML baru dengan nama register.html di dalam folder template. Secara garis besar, isi berkas tersebut adalah command         pembuatan form yang meminta username dan password dari user. Selanjutnya, dilakukan routing /todolist/register dengan cara mengimpor fungsi register di urls.py     di folder todolist, lalu menambahkan path yang sesuai di urlpatterns.

    Selanjutnya, dibuat pula form login. Hal ini dilakukan dengan membuat fungsi login pada views.py dan melakukan impor uthenticate dan login. Kemudian,               ditambahkan potongan kode untuk mengisi fungsi login yang berfungsi untuk melakukan otentikasi user. Selanjutnya, dibuat pula berkas login.html yang secara         garis besar berisi form yang meminta username dan password. Selanjutnya, juga dilakukan routing todolist/login dengan mengimpor fungsi login di urls.py yang       ada di todolist dan menambahkan path yang sesuai di urlpatterns.

    Selanjutnya, dibuat pula fitur logout. Hal ini dilakukan dengan membuat fungsi logout pada views.py dan melakukan impor logout. Fungsi logout akan menerima         parameter request dan mengembalikan redirect ke halaman login. Selanjutnya, tambahkan button Log Out di halaman HTML yang dikaitkan dengan fungsi logout yang       sudah dibuat untuk melakukan mekanisme logout. Selanjutnya, dilakukan routing dengan cara mengimport fungsi logout di urls.py yang ada di folder todolist dan       menambahkan path yang sesuai di urlpatterns.
  
5. <p align="justify">Poin kelima dilakukan dengan membuat sebuah berkas HTML dengan nama todolist.html di dalam folder templates. Berkas HTML secara umum berisi judul halaman, username dari user yang sedang log in, lalu melakukan iterasi untuk setiap elemen yang ada pada model Task. Field-field tersebut akan ditampilkan dalam bentuk tabel sehingga digunakan tag table. Selanjutnya, ditambahkan tombol tambah task baru yang nantinya akan dikaitkan dengan fungsi pembuatan task. </p>
 
6. <p align="justify">Poin keenam dilakukan dengan membuat sebuah fungsi dengan nama create_task di views.py. Fungsi ini akan menerima parameter request dan mengembalikan redirect ke halaman html bernama create-task. Fungsi ini melakukan pengambilan dan penyimpanan data yang dimasukkan oleh user sebagai input. Kemudian, dibuat sebuah berkas HTML yang secara garis besar berisi form untuk meminta nama dan deskripsi dari tag. Selanjutnya, dilakukan routing url dengan mengimpor fungsi create_Task di berkas urls.py yang ada di folder todolist dan menambahkan path ke variable urlpatterns.</p>
  
7. <p align="justify">Routing halaman telah dilakukan pada langkah sebelumnya, yaitu dengan mengimport fungsi yang diinginkan, lalu menambahkan path fungsi tersebut ke variable urlpatterns.</p>
  
8. <p align="justify">Deployment ke Heroku dilakukan dengan membuat sebuah aplikasi di laman Heroku dan membuat repository secrets berisi nama aplikasi Heroku dan API key dari aplikasi Heroku. Setelah itu, workflow yang tadinya gagal akan dijalankan kembali dan deployment selesai. </p>
  
9. <p align="justify">Poin terakhir dilakukan dengan membuat akun langsung setelah dapat mengakses web dari aplikasi Heroku, lalu menambahkan task pada masing-masing akun yang telah dibuat. </p>
  

<br />
