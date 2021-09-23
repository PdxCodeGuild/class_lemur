from django.urls import path
from . import views


app_name = 'Poo_Talk_posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
]