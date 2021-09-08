from django.urls import path

from . import views

app_name = 'contacts_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.contact, name='city')
]  