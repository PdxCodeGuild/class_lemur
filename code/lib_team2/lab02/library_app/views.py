from django.shortcuts import redirect, render

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
    book_out = request.POST['book_out']

    return redirect('library_app:index')