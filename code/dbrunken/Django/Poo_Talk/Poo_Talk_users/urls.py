from django.urls import path
from . import views

app_name = 'Poo_Talk_users'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('new_user/', views.new_user, name='new_user')
]