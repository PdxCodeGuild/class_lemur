from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete_item/', views.indexDelete, name='delete_item')
]