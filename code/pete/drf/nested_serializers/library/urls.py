from django.urls import path

from . import views

urlpatterns = [
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>/', views.AuthorDetail.as_view()),
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
]