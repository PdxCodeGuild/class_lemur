from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('make_post/', views.make_post, name="make_post")
]
