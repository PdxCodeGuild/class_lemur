from django.shortcuts import render, get_object_or_404,redirect
from datetime import datetime
from .models import Post, User
from django.template import loader
from django.urls import reverse
# Create your views here.
def landing(request):
    posts=Post.objects.all()
    return render(request, 'chirp/landing.html', posts)