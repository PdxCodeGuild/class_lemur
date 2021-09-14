from django.shortcuts import render
from django.shortcuts import redirect
from .models import Groceries
from .forms import GroceriesForm

# Create your views here.


def index(request):
    form = GroceriesForm()
    groceries = Groceries.objects.filter(cleared=False)
    bought = Groceries.objects.filter(cleared=True)
    context = {'groceries': groceries,
               'form':form,
               'bought':bought,
               }
    # Add an item
    if request.method == 'POST':
        form = GroceriesForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'home.html', context)

def indexDelete(request,pk):
    delete_item = Groceries.objects.get(id=pk)
    if request.method == 'POST':
        delete_item.delete()
        return redirect('index')
    # context = {'delete':delete_item}
    # return render(request, 'delete_item.html', context)
