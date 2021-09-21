from django.urls import path
from . import views

app_name = 'app_chirp' # for namespacing
urlpatterns = [
    path('', views.landing, name='landing'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('user/<int:id>',views.profile, name='profile'),
]