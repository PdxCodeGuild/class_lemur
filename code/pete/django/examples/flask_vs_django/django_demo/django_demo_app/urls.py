from django.urls import path
from . import views

app_name = 'django_demo_app'

urlpatterns = [
    # in place of @app.route('/')
    # decorator from flask
    path('', views.index, name='index'),
]