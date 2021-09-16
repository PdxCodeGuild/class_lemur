from django.urls import path
from . import views

app_name = 'list'

urlpatterns= [
    path('', views.index, name="index"),
    path('', views.complete, name="complete"),
    path('', views.delete, name = "delete"),

]