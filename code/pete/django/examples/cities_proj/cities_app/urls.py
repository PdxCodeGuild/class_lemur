from django.urls import path

from . import views

app_name = 'cities_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.city, name='city'),
    path('<slug:slug>/update/', views.update_city, name='update_city'),
]