from django.shortcuts import render, get_object_or_404,redirect
from datetime import datetime
from .models import Book, Genre, Tracking, Author, User
from django.template import loader
from django.urls import reverse

def index(request):
    if request.method == 'POST':
        print(request.POST) 
        data = dict(request.POST)
        print(data)
        title=request.POST.get('title')
        
        return redirect('/')
    books = {
        'titles':Book.objects.all(), # get all the Books 
    }
    print(books)
    return render(request, 'Lib_App/index.html', books)
    