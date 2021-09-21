from django.urls import path
from .views import AuthorCreateView, AuthorUpdateView, AuthorDeleteView

app_name = 'Poo_Talk_posts'
urlpatterns = [
    path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    path('author/<int:pk>/delete', AuthorDeleteView.as_view(), name='author-delete'),
]