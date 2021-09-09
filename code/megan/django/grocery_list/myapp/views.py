from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse

from .models import GroceryItem

def index(request): 

    context = {
        'all_items': GroceryItem.objects.all(),
        'completed_list' : GroceryItem.objects.filter(complete=True),
        'incomplete_list' : GroceryItem.objects.filter(complete=False)
    }

    return render(request, 'myapp/index.html', context)

def new_item(request):
    item = request.POST['item']
    groceryitem = GroceryItem(item=item)
    groceryitem.save()

    return HttpResponseRedirect(reverse('myapp:index'))


def completed_item(request, id):
    item = request.POST['id']
    completed = GroceryItem.objects.get(id=id)
    completed.completed = True
    completed.save()

    return HttpResponseRedirect(reverse('myapp:index'))

	
def delete_item(request, id):
    item = request.POST['id']
    items = GroceryItem.objects.get(id=id)
    items.delete()

    return HttpResponseRedirect(reverse('myapp:index'))

