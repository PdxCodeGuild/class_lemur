from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('new_item/', views.new_item, name='new_item'),
    path('delete_item/<int:id>', views.delete_item, name='delete_item'), 
    path('completed_item/<int:id>', views.completed_item, name='completed_item'), 
]

