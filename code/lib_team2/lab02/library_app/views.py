from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Book, Author, Checkout

# Create your views here.
def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    checkouts = Checkout.objects.filter(checkout=True)
    checkins = Checkout.objects.filter(checkout=False)
    context={
        'books' : books,
        'authors' : authors,
        'checkouts': checkouts,
        'checkins' : checkins,
    }
    return render(request, 'library_app/index.html', context)

def checkout(request):
    if request.method == 'POST':
        title_from_input = request.POST['title'] # title
        user = request.POST['user']
        timestamp = request.POST['time_stamp']
        # get the book where title is title
        book_obj = Book.objects.get(title = title_from_input)  
        # kwargs are a dictionary { 'title': title}

        Checkout.objects.create(
            book = book_obj,
            user = user,
            timestamp = timestamp,
            checkout = True,
        )

    print(request.POST)
    return redirect('library_app:index')