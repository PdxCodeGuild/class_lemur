from django.urls import path
from . import views

app_name = 'daycare'

urlpatterns = [
    path('', views.index, name='index'),
    path('drop-off/', views.drop_off, name='drop_off'),
    path('owner/<int:id>/', views.owner_profile, name='owner_profile'),
]