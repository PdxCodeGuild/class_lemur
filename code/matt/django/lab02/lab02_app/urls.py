from django.urls import path

from . import views

app_name = "lab02_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/<str:name>/', views.checkout, name='checkout'),
    path('check/<int:id>/', views.checkin, name='checkin'),
]
