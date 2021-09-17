from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('log_out/', views.log_out, name="log_out"),
    path('log_in/', views.log_in, name="log_in"),
    path('register_user/', views.register_user, name="register_user"),
]
