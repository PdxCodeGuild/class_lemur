from django.shortcuts import render
from .models import Book, Author
# Create your views here.

def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    print(books)
    print(authors)
    context = {
        'books': books,
        'author': authors
    }
    return render(request, 'library/index.html', context)


