from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Book, Author, Checkout

# Create your views here.
def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    checkouts = Checkout.objects.all()
    context = {
        'books':books,
        'authors':authors,
        'checkouts':checkouts,
    }
    return render(request, 'lib_app/index.html', context)

def status(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    checkouts = Checkout.objects.all()
    context = {
        'books':books,
        'authors':authors,
        'checkouts':checkouts,
    }
    return render(request, 'lib_app/status.html', context)

def check_out(request, pk):
    checked_book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        checked_book.checked = True
        return redirect('index')