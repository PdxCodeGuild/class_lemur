from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('get-todos/', views.get_todos, name='get_todos'),
    path('add-todo/', views.add_todo, name='add_todo'),
]