from django.shortcuts import render, get_object_or_404,redirect
from datetime import datetime
from .models import Book, Genre, Tracking, Author
from django.template import loader
from django.urls import reverse

def index(request):
    if request.method == 'POST':
        # If there's a POST request, that means the user
        # has submitted a new Lib_App for the database
        # How do you parse it?
        print(request.POST) # this will show the post request's
        # QueryDict, a dictionary-like object with the contents
        # of the form data
        data = dict(request.POST) # Optionally, turn the QueryDict
        print(data) # into a plain Python dictionary
        title=request.POST.get('title')
        Book.objects.create(
            title=title,
            
        )
        return redirect('/')
    books = {
        'titles':Book.objects.all() # get all the Books 
    }
    return render(request, 'Lib_App/index.html', context=books)