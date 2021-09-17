from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Book, Author, Checkout

# Create your views here.
def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    checkouts = Checkout.objects.filter()
    context={
        'books' : books,
        'authors' : authors,
        'checkouts': checkouts,
    }
    return render(request, 'library_app/index.html', context)

def checkout(request):
    if request.method == 'POST':
        book = request.POST['book']
        user = request.POST['user']
        time_stamp = request.POST['time_stamp']
        book.checkout = True
    print(request.POST)
    return redirect('library_app:index')