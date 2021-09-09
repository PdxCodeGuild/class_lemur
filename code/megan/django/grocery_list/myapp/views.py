from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse

from .models import GroceryItem

def index(request): 

    myinstances = GroceryItem.objects.all()

    context = {
        'myinstances': myinstances,
        'completed_list' : GroceryItem.objects.filter(incomplete=False),
        'incomplete_list' : GroceryItem.objects.filter(incomplete=True)

    }

    return render(request, 'myapp/index.html', context)

def new_item(request):
    item = request.POST['item']
    groceryitem = GroceryItem(item=item)
    groceryitem.save()

    return HttpResponseRedirect(reverse('myapp:index'))


def complete(request, id):
# 	  use the id to get the object from the database
# 	  change its completed attribute to False
#     save it 
#     return HttpResponseRedirect(reverse('myapp:index'))
    ...
	
def delete(request, id):
	# use the id to get the object from the database
	# delete it
	# redirect back to the home page
	...
