from django.shortcuts import render

from .models import Book, Author

# Create your views here.
def index(request):
    book = Book.objects.all()
    author = Author.objects.all()
    context={
        'book' : book,
        'author' : author,
    }
    return render(request, 'library_app/index.html', context)

