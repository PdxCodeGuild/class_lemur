from django.urls import path
from . import views

app_name = 'Poo_Talk_users'
urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('new_user/', views.new_user, name='new_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
]