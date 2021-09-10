from django.shortcuts import render, get_object_or_404

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

		# Save the new GroceryItem to the databse!

		# What else?  Return, redirect?  It's up to you!

	# Here you'll put the code that you want to run for a GET request
	# How do you want to get the necessary items from the database?
	# Here are 3 different queries that return different QuerySets
	# You can use one of these or a combination to put into your context
	# dictionary and render the template

	grocery_list = GroceryItem.objects.all() # get all the GroceryItems
	completed_list = GroceryItem.objects.filter(completed=True) # get the completed GroceryItems
	incomplete_list = GroceryItem.objects.filter(completed=False) # get the incomplete GroceryItems

	context = {'grocery_list': grocery_list} # the context dictionary will have all the objects
	# you want to render in your template
	# the return line will render the template
	return render(request, 'list_app/index.html', context)


def complete(request, id):
    return render(request, 'list_app/index.html')
	# use the id to get the object from the database
	# change it's completed attribute to True
	# save it
	# redirect back to the home page

def delete(request, id):
    grocery_list = GroceryItem.objects.all() # get all the GroceryItems
    completed_list = GroceryItem.objects.filter(completed=True) # get the completed GroceryItems
    incomplete_list = GroceryItem.objects.filter(completed=False) # get the incomplete GroceryItems
    context = {'grocery_list': grocery_list} # the context dictionary will have all the objects
    return render(request, 'list_app/delete.html', context)
	# use the id to get the object from the database
	# delete it
	# redirect back to the home page
	