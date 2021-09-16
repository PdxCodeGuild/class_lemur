from django.urls import path 
from . import views

app_name = 'library_app'

urlpatterns=[
    path('library_app', views.index, name='index')
]