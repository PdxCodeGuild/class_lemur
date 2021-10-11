from django.urls import path
from . import views

app_name='posts_app'

urlpatterns = [
    path('', views.feed, name='feed'),
    # path('post/', views.post, name='post'),
]