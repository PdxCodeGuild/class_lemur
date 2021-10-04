from django.urls import path

from . import views

urlpatterns = [
    path('', views.CityList.as_view()),
    path('<int:pk>/', views.CityDetail.as_view()),
]