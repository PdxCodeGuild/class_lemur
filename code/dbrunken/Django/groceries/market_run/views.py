from django.shortcuts import render
from .models import Item

def index(request):
    items = Item.objects.all()

    context = {
        'grocery_items' : items
    }
    return render(request, 'market_run/index.html', context)

def base(request):
    