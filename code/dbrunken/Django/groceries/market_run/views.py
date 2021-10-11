from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Item

def index(request):
    items = Item.objects.all()
    bought_groceries = Item.objects.filter(bought=True)
    missed_items = Item.objects.filter(bought=False)
    added_item = Item.objects.filter(bought=False)

    context = {
        'grocery_items': items,
        'bought_groceries': bought_groceries,
        'missed_items': missed_items,
        'added_item':added_item
    }
    return render(request, 'market_run/index.html', context)

def bought(request, id):
    item = get_object_or_404(Item, id=id)
    item.bought = True
    item.date_bought = timezone.now()
    item.save()
    return redirect('market_run:index')

def added_item(request):
    new_item = request.POST['new_item']
    Item.objects.create(item=new_item)
    return redirect('market_run:index')