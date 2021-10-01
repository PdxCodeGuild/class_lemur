from django.shortcuts import redirect, render, get_object_or_404

from .models import Author, Book, Checkout, Genre


def index(request):
    authors = Author.objects.order_by('name')
    books = Book.objects.all
    checkout = Checkout.objects.all
    genre = Genre.objects.all

    if request.method == 'POST':
        if 'checkout' in request.POST:
            book = Book.objects.filter(title=request.POST.get('book'))[0]
            user = request.POST.get('user_name')
            time = request.POST.get('checkout_time')
            checkouts = Checkout.objects.filter(checkout=True)
            for checkout_book in checkouts:
                if book == checkout_book.book:
                    author = book.author
                    context = {
                        'book': book,
                        'author': author
                    }
                    return render(request, 'lab02_app/checkout.html',  context)

            Checkout.objects.create(
                book=book,
                user=user,
                checkout=True,
                time=time,
            )

        return redirect("lab02_app:index")

    context = {
        'authors': authors,
        'books': books,
        'checkout': checkout,
        'genre': genre
    }
    return render(request, 'lab02_app/index.html', context)


def checkout(request, name):
    author = get_object_or_404(Author, name=name)
    return render(request, 'lab02_app/checkout.html', {'author': author})


def checkin(request, id):
    book = get_object_or_404(Checkout, id=id)
    book.checkout = False
    book.save()
    return redirect('lab02_app:index')
