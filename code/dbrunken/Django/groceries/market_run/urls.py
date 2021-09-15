from django.urls import include, path
from . import views

app_name = 'market_run'
urlpatterns = [
    path('', views.index, name="index"),
]