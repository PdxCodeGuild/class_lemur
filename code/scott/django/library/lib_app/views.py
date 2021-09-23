from django.shortcuts import render
from django.shortcuts import redirect
from .models import Book, Checkout
from .forms import CheckoutForm

# Create your views here.
def index(request):
    form = CheckoutForm()
    all_books = Book.objects.all()
    all_checkouts = Checkout.objects.all()
    context = {
        'all_checkouts': all_checkouts,
        'all_books' : all_books,
        'form' : form,
    }
    
    return render(request, 'lib_app/index.html', context)

def check(request):
    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()        
    
    return redirect('lib_app:index')
    