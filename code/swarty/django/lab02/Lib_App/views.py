from django.shortcuts import render, get_object_or_404,redirect
from datetime import date, datetime, timedelta
from .models import Book, Genre, Tracking, Author, User
from django.template import loader
from django.urls import reverse
from django.views import generic

def get_due_date():
    return date.today() + timedelta(days=20)

def index(request):
    if request.method == 'POST':
        bookid=Book.objects.get(pk=request.POST['checkout'])
        print(bookid.checked_out)
        if bookid.checked_out == True:
            bookid.checked_out=False
        else:
            bookid.checked_out = True
        bookid.save()

    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()
    context = {
        'titles':Book.objects.all(), # get all the books 
        'num_books': num_books,
        'num_authors': num_authors,
        'traces':Tracking.objects.all()
    }
    return render(request, 'Lib_App/index.html', context)

def checkout(request,pk):
    bookid=get_object_or_404(Book, pk=pk)
    bookid.checked_out = True
    tracking = Tracking.objects.create(
        user=request.user
    )
    
    tracking.title.set([bookid.id]) #because manytomany
    print(bookid.checked_out)
    bookid.save()
    return redirect('Lib_App:index')

def checkin(request,pk):
    bookid=get_object_or_404(Book, pk=pk)
    bookid.checked_out = False
    print(bookid.Title.all())
    trace=bookid.Title.get(title=pk, checkin=None)
    trace.checkin=datetime.now()
    trace.save()
    bookid.save()
    return redirect('Lib_App:index')

class BookListView(generic.ListView):
    model = Book

    def get_context_data(self, **kwargs):
        #  get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        return context

class BookDetailView(generic.DetailView):
    model = Book


