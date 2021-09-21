from django.urls import path
from . import views

app_name = 'lib_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('check/', views.check, name='check'),
]

