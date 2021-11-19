from django.urls import path
from . import views

app_name = 'Lib_App' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('checkout/<int:pk>', views.checkout, name='checkout'),
    path('checkin/<int:pk>', views.checkin, name='checkin')
]