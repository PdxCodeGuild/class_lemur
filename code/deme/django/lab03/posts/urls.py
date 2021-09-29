from django.urls import path
from . import views
app_name = 'posts'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('user_profile/<int:id>', views.user_profile, name = 'user_profile')
]