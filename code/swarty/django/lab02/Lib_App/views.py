from django.shortcuts import render, get_object_or_404,redirect
from datetime import datetime
from .models import Book, Genre, Tracking, Author, User
from django.template import loader
from django.urls import reverse
from django.views import generic

def index(request):
    if request.method == 'POST':
        
        if Book.checked_out == True:
            Book.checked_out == False
        if Book.checked_out == False:
            Book.checked_out == True

    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()
    context = {
        'titles':Book.objects.all(), # get all the books 
        'num_books': num_books,
        'num_authors': num_authors,
    }
    return render(request, 'Lib_App/index.html', context)

class BookListView(generic.ListView):
    model = Book

    def get_context_data(self, **kwargs):
        #  get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        return context

class BookDetailView(generic.DetailView):
    model = Book


