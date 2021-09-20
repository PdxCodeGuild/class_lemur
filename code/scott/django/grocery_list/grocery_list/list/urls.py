from django.urls import path

from . import views

# app_name = 

urlpatterns = [
    path('', views.index, name='home'),
    path('<str:pk>/', views.indexDelete, name='delete_item'),
    path('<str:pk>/', views.indexPurchased, name='purchased_item')
]
