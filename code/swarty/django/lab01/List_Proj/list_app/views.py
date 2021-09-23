from django.shortcuts import render, get_object_or_404,redirect
from datetime import datetime
from .models import GroceryItem
from django.template import loader
from django.urls import reverse

def index(request):
	if request.method == 'POST':
		# If there's a POST request, that means the user
		# has submitted a new GroceryItem for the database
		# How do you parse it?
		print(request.POST) # this will show the post request's
		# QueryDict, a dictionary-like object with the contents
		# of the form data
		data = dict(request.POST) # Optionally, turn the QueryDict
		print(data) # into a plain Python dictionary
		title=request.POST.get('title')
		# if GroceryItem.title != title:
		GroceryItem.objects.create(
			title=title,
			creation=datetime.now()
		)
		return redirect('/')

		

	# Here you'll put the code that you want to run for a GET request
	# How do you want to get the necessary items from the database?
	# Here are 3 different queries that return different QuerySets
	# You can use one of these or a combination to put into your context
	# dictionary and render the template

	grocery_list = GroceryItem.objects.all() # get all the GroceryItems
	completed_list = GroceryItem.objects.filter(completed=True) # get the completed Items
	incomplete_list = GroceryItem.objects.filter(completed=False) # get the incomplete Items

	context = {
		'all': grocery_list, 
		'completed':completed_list, 
		'incomplete': incomplete_list,
		} # the context dictionary will have all the objects
	# you want to render in your template
	# the return line will render the template
	return render(request, 'list_app/index.html', context)


def complete(request):
	print(request.POST)
	id=int(request.POST.get('id'))
	item= GroceryItem.objects.get(id=id)
	item.completion=datetime.now()
	item.completed=True
	item.save()
	return redirect('/')

def delete(request):
	print(request.POST)
	id=int(request.POST.get('id'))
	item=GroceryItem.objects.get(id=id)
	item.delete()
	return redirect('/')
