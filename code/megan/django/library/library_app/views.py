from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404

from .models import Book, Author, Checked
from .forms import LibraryForm

def index(request):

    books = Book.objects.all()
    authors = Author.objects.all()
    # checked = Checked.objects.all()

    context = {
        'books': books,
        'authors': authors,
        'checked': Checked.objects.all(),
    }

    return render(request, 'library_app/index.html', context)


def form(request):
    if request.method == 'POST':
            
        form = LibraryForm(request.POST)

        if form.is_valid():

            form.save()

        return redirect('library_app:index')

    form = LibraryForm()

    context = {
        'form': form,
    }

    return render(request, 'library_app/check.html', context)

def returning(request, id):

    id = request.POST['id']
    returned = Checked.objects.get(id=id)
    returned.checked_out = False
    returned.save()

    return redirect('library_app:index')

