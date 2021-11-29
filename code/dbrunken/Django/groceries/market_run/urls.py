from django.urls import include, path
from . import views
# from .views import DeleteItem

app_name = 'market_run'

urlpatterns = [
    path('', views.index, name="index"),
    path('added_item/', views.added_item, name="added_item"),
    path('<int:id>/bought/', views.bought, name="bought"),
    path('<int:id>/delete_item/', views.delete_item, name="delete_item")
]