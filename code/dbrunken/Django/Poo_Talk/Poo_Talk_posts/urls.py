from django.urls import path
from . import views

app_name = 'Poo_Talk_posts'
urlpatterns = [
    path('', views.posts, name='posts')
]