from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('new_item/', views.new_item, name='new_item')
]

