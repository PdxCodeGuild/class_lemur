from django.shortcuts import render

from django.utils import timezone

from .forms import GroceryItemForm

from .models import GroceryItem


def index(request):
	if request.method == 'POST':
		print("stringgggg")
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

		# Save the new GroceryItem to the databse!

		# What else?  Return, redirect?  It's up to you!

	# Here you'll put the code that you want to run for a GET request
	# How do you want to get the necessary items from the database?
	# Here are 3 different queries that return different QuerySets
	# You can use one of these or a combination to put into your context
	# dictionary and render the template

	grocery_list = GroceryItem.objects.all() # get all the GroceryItems
	completed_list = GroceryItem.objects.filter(completed=True) # get the completed GroceryItems
	incomplete_list = GroceryItem.objects.filter(completed=False) # get the completed GroceryItems

	form = GroceryItemForm()

	context = {"grocery_list" : grocery_list, "grocery_item_form" : form} # the context dictionary will have all the objects
	# you want to render in your template
	# the return line will render the template
	return render(request, 'list/index.html', context)

"""
Note: there are multiple ways to complete/delete GroceryItems
The following is just a suggestion
"""

def complete(request, id):
	if request.method == 'GET':
		print("stringgggg")
		description = request.GET['description']
		GroceryItem.objects.create(description = description, created_date = timezone.now())
		# If there's a POST request, that means the user
		# has submitted a new GroceryItem for the database
		# How do you parse it?
		print(request.GET) # this will show the post request's
		# QueryDict, a dictionary-like object with the contents
		# of the form data
		data = dict(request.GET) # Optionally, turn the QueryDict
		print(data) # into a plain Python dictionary
	# use the id to get the object from the database
	# change it's completed attribute to True
	# save it
	# redirect back to the home page
	

def delete(request, id):
	description = request.GET['description']
	GroceryItem.objects.delete(description = description)
	description.delete()
