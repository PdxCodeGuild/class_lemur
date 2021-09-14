from django.shortcuts import render, reverse, HttpResponseRedirect

from .models import Book, Author, User, Checked


def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()

    context = {
        'books': books,
        'authors': authors,
        # 'out': Book.objects.filter(checked_out=True),
        # 'in': Book.objects.filter(checked_out=False),
    }

    return render(request, 'library_app/index.html', context)


def checked(request):
    books = Book.objects.all()
    users = User.objects.all()

    context = {
        'books': books,
        'users': users
    }

    # id = request.POST['name']
    # brought_back = Book.objects.get(id=id)
    # brought_back.checked_out = False
    # brought_back.save()

    # return HttpResponseRedirect(reverse('library_app:index'), context)

    return render(request, 'library_app/check.html', context)

def new_user(request):
    # if request.method == 'POST':

        name = request.POST.get('id')
        print("You did a post request!")
        added_user = User(name=name)
        added_user.save()

        return HttpResponseRedirect(reverse('library_app:checked'))


def records(request):
    users = User.objects.all()
    books = Book.objects.all()
    records = Checked.objects.all()

    context = {
        'books': books,
        'users': users,
        'records': records
    }

    return render(request, 'library_app/records.html', context)