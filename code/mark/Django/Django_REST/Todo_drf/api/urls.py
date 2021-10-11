from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TodoList.as_view()),
    path('<int:pk>', views.TodoDetails.as_view())
]
