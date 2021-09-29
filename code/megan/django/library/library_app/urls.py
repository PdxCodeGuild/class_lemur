from django.urls import path
from . import views

app_name = 'library_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('returning/<int:id>', views.returning, name='returning'),
]
