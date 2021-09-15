from django.urls import path

from . import views

app_name = 'grocery_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('complete/<int:id>/', views.complete, name='complete'),
]