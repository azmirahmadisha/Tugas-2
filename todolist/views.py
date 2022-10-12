
import datetime
from pydoc import describe
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from todolist.models import TodoListItem
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound

from todolist.models import TodoListItem

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = TodoListItem.objects.filter(user=request.user)
    context = {
    'data_todolist': data_todolist,
    }
    return render(request, "todolist.html", context)

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

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        judul = request.POST.get("title")
        deskripsi = request.POST.get("description")
        add_todolist = TodoListItem(user=request.user, title=judul, description=deskripsi, date=datetime.datetime.now())
        add_todolist.save()
        return redirect('todolist:show_todolist')
    return render(request, 'create-task.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login/')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def deleteTodo(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todolist/')

@login_required(login_url='/todolist/login/')
def updateTodo(request, i):
    item = TodoListItem.objects.get(user=request.user, pk = i)
    item.isFinished = not item.isFinished
    item.save()
    return HttpResponseRedirect('/todolist/')

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = TodoListItem.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    context = {
    'nama': 'Adish',
    }
    return render(request, "todolist_ajax.html", context)

# def add_todolist_ajax(request: HttpRequest):
#      if request.method == "POST":
#          title = request.POST.get("title")
#          date = request.POST.get("date")
#          description = request.POST.get("description")

#          new_barang = TodoListItem(
#              title=title,
#              date=date,
#              description=description,
#          )
#          new_barang.save()
#          return HttpResponse(
#              serializers.serialize("json", [new_barang]),
#              content_type="application/json",
#          )

#      return HttpResponseRedirect('/todolist/ajax')

@login_required(login_url='/todolist/login/')
def add_todolist_ajax(request):
    if request.method == "POST":
        judul = request.POST.get("title")
        deskripsi = request.POST.get("description")
        add_todolist = TodoListItem(user=request.user, title=judul, description=deskripsi, date=datetime.datetime.now())
        add_todolist.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()