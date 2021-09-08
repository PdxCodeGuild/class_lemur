from django.urls import path

from . import views

app_name = 'cities_app'

urlpatterns = [
    path('', views.index, name='index'),
    # example path: localhost:8000/kansas-city
    path('<slug:slug>/', views.city, name='city'),
    # example path: localhost:8000/kansas-city/update
    path('<slug:slug>/update/', views.update_city, name='update_city'),
]