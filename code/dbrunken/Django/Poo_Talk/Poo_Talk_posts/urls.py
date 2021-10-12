from django.urls import path
from . import views
# from Poo_Talk_users import views


app_name = 'Poo_Talk_posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    # path('login/', views.login, name='login_user'),
    # path('new_user/', views.new_user, name='new_user')
]