from django.shortcuts import render
from .models import Book, Author, Checkout, Genre

def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'books': books,
        'author': authors,
    }
    return render(request, 'library/index.html', context)

def checkout(request):
    books = Book.objects.all()
    if request.method == 'POST':
        user = request.POST.get("user")
        book = request.POST.get("name")
        print('Book Title: ' + book)
        checkout = True
        Checkout.objects.create(checkout=checkout, book_title=book, user=user)
        book_edit = books.get(title=book)
        book_edit.checked_out = checkout
        book_edit.save()
    return index(request)

def checkin(request):
    books = Book.objects.all()
    if request.method == 'POST':
        book = request.POST.get("name")
        
        filtered_book = Checkout.objects.filter(book_title=book, checkout=True).order_by('-timestamp').first()
        user = filtered_book.user
        checkout = False
        Checkout.objects.create(checkout=checkout, book_title=book, user=user)
        book_edit = books.get(title=book)
        book_edit.checked_out = checkout
        book_edit.save()
    return index(request)

def status(request):
    checkouts = Checkout.objects.all()
    context = {
        'checkouts': checkouts
    }
    return render(request, 'library/status.html', context)