from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('status/', views.status, name='status'),
    path('', views.check_out, name='check_out')
]

