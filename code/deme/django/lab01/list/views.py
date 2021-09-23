from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import GroceryItemForm

from .models import GroceryItem


def index(request):
	if request.method == 'POST':
		description = request.POST['description']
		GroceryItem.objects.create(description = description, created_date = timezone.now())
		# If there's a POST request, that means the user
		# has submitted a new GroceryItem for the database
		# How do you parse it?
		print(request.POST) # this will show the post request's
		# QueryDict, a dictionary-like object with the contents
		# of the form data
		data = dict(request.POST) # Optionally, turn the QueryDict
		print(data) # into a plain Python dictionary


	grocery_list = GroceryItem.objects.all() # get all the GroceryItems
	completed_list = GroceryItem.objects.filter(completed=True) # get the completed GroceryItems
	incomplete_list = GroceryItem.objects.filter(completed=False) # get the completed GroceryItems

	form = GroceryItemForm()

	context = {"grocery_list" : grocery_list, "grocery_item_form" : form} # the context dictionary will have all the objects
	# you want to render in your template
	# the return line will render the template
	return render(request, 'list/index.html', context)

def complete(request, id):
	item = get_object_or_404(GroceryItem, id=id) #return grocery item or 404 error
	item.completed = True
	item.completed_date = timezone.now() #set completed date according to timezone
	item.save()
	return redirect('list:index')

def delete(request, id):
	item = get_object_or_404(GroceryItem, id=id) #return grocery item or 404 error
	item.delete()
	return redirect('list:index')
