from django.urls import path
from todolist.views import show_todolist
from todolist.views import create_task
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import register
from todolist.views import deleteTodo
from todolist.views import updateTodo

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create-task'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('deleteTodoItem/<int:i>/', deleteTodo, name='deleteTodo'), 
    path('updateItem/<int:i>/', updateTodo, name='updateTodo'), 
]