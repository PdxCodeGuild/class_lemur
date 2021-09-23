from django.urls import path

from . import views

app_name = 'list'

urlpatterns = [
    path('', views.index, name='home'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    path('purchased_item/<int:id>/', views.purchased_item, name='purchased_item')
]
