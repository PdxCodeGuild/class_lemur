from django.urls import path

from . import views

app_name = 'lab03_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('chirp/', views.chirp, name='chirp'),
    path('chirp_comments/<int:id>/', views.chirp_comments, name='chirp_comments'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('likes/<int:id>/', views.likes, name='likes'),
]
