from django.urls import path
from . import views

app_name = 'library_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('checked/', views.checked, name='checked'),
    path('new_user/', views.new_user, name='new_user'),
    path('records/', views.records, name='records'),
]
