from django.urls import path
from . import views

urlpatterns= [
    path('', views.index),
    # path('', admin.site.urls),
    path('', views.index, name="index"),
    path('', views.complete, name="complete"),
    path('', views.delete, name = "delete"),

]