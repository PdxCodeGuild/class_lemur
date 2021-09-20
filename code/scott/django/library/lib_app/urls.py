from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('status/', views.status, name='status'),
    path('<int:pk>', views.check_out, name='checkout')
]

