from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('Poo_Talk_users.urls')),
    path('posts/', include('Poo_Talk_posts.urls'))
]
