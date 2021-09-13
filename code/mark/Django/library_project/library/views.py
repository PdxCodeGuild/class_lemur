from django.shortcuts import render
from .models import Book, Author, Checkout

def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    checkouts = Checkout.objects.all()
    context = {
        'books': books,
        'author': authors,
        'checkouts': checkouts
    }
    return render(request, 'library/index.html', context)

def checkout(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        book = request.POST.get("name")
        checkout = True
        Checkout.objects.create(checkout=checkout, book=book, user=user)
    return index(request)

def checkin(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        book = request.POST.get("name")
        books = Checkout.objects.filter(book=book, checkout=True).order_by(timestamp).first()
        # books = Checkout.objects.filter(book=book, checkout=True).order_by(Checkout.timestamp).first()
        print(books)
        checkout = False
        Checkout.objects.create(checkout=checkout, book=book, user=user)
    return index(request)

def status(request):
    checkouts = Checkout.objects.all()
    context = {
        'checkouts': checkouts
    }
    return render(request, 'library/status.html', context)