from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path('', views.index, name='index'),
    path('house/<str:name>/', views.house, name='house'),
]