from django.shortcuts import redirect, render, get_object_or_404

from .models import Author, Book, Checkout


def index(request):
    authors = Author.objects.order_by('name')
    books = Book.objects.all
    checkout = Checkout.objects.all
    if request.method == 'POST':
        if 'checkout' in request.POST:
            book = Book.objects.filter(title=request.POST.get('book'))[0]
            user = request.POST.get('user_name')
            time = request.POST.get('checkout_time')
            checkouts = Checkout.objects.filter(checkout=True)
            for book1 in checkouts:
                if book != book1:
                    Checkout.objects.create(
                        book=book,
                        user=user,
                        checkout=True,
                        time=time,
                    )

        if 'checkin' in request.POST:
            books = Checkout.objects.filter(checkout=True)

            for book in books:
                check = request.POST.get(f'{book.book}checkout')
                if check:
                    book.checkout = False
                    book.save()

        return redirect("/")

    context = {
        'authors': authors,
        'books': books,
        'checkout': checkout
    }
    return render(request, 'lab02_app/index.html', context)


def checkout(request, name):
    author = get_object_or_404(Author, name=name)
    return render(request, 'lab02_app/checkout.html', {'author': author})
