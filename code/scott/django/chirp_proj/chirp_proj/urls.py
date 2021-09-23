from django.urls import include 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts_app.urls')),
    path('', include('users_app.urls')),
]
