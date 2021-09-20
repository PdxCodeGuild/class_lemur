from django.urls import path
from . import views

app_name = 'Poo_Talk_users'
urlpatterns = [
    path('', views.index, name='index')
]