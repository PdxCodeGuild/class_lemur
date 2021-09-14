from django.shortcuts import render, reverse, HttpResponseRedirect

from .models import Book, Author, User

def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()

    context = {
        'books': books,
        'authors': authors,
        'out': Book.objects.filter(checked_out=True),
        'in': Book.objects.filter(checked_out=False),
    }

    return render(request, 'library_app/index.html', context)

def checked(request):
    users = User.objects.all()
    books = Book.objects.all()

    context = {
        'books': books,
        'users': users
    }

    return render(request, 'library_app/check.html', context)

def new_user(request):
    name = request.POST['name']
    user = User(name=name)
    user.save()

    return HttpResponseRedirect(reverse('myapp:index'))

def records(request):
    users = User.objects.all()
    books = Book.objects.all()

    context = {
        'books': books,
        'users': users
    }

    return render(request, 'library_app/records.html', context)