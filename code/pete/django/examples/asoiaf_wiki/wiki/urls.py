from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('', views.index, name='index'),
    path('house/<int:pk>/', views.HouseView.as_view(), name='house'),
    # path('house/<str:name>/', views.house, name='house'),
]