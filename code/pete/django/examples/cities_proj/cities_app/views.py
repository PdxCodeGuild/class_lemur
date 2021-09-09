from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from random import choice, random

from .models import City


def random_color():
    return choice([
        'gray',
        'red',
        'yellow',
        'green',
        'blue',
        'indigo',
        'purple',
        'pink',
    ])

# @app.index('/', methods=['GET', 'POST']) the decorator you would use if this was flask
def index(request):

    if request.method == 'POST': # if you submit the form to the same view
        # request.POST and request.FILES are dictionary-like objects
        # containing all the "named" data from the form
        # inputs must have a name="" attribute to show up in these objects!
        print(request.POST) # plain text from inputs
        print(request.FILES) # file uploads

        # get all the data out of the form!
        name = request.POST.get('name')
        country = request.POST.get('country')
        food = request.POST.get('food')
        population = request.POST.get('population')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')

        City.objects.create( # Model.object.create will create a new row in the database
            name=name,
            country=country,
            food=food,
            population=population,
            description=description,
            photo=photo,
            slug=slugify(name) # the slugify function (imported above),
            # returns a "slugified" version of a string, i.e.:
            # if name = 'Rio de Janeiro'
            # slug = 'rio-de-janeiro'
        )
        return redirect('/') # redirects back to the home page
        
    cities = City.objects.all()
    print(cities) # <QuerySet [<City: Portland>, <City: Rhodes>, <City: Seville>, <City: Seoul>]>
    context = {
        'cities': cities,
    }
    return render(request, 'cities_app/index.html', context)

def city(request, slug): # the id comes from <int:id> in the urlpatterns in urls.py
    # city = City.objects.get(slug=slug)
    city = get_object_or_404(City, slug=slug) # prevents django from crashing if the object does not exist
    color = random_color()
    return render(request, 'cities_app/city.html', {'city': city, 'color': color})

def update_city(request, slug): # the id comes from <int:id> in the urlpatterns in urls.py
    city = get_object_or_404(City, slug=slug) # prevents django from crashing if the object does not exist

    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        country = request.POST.get('country')
        food = request.POST.get('food')
        population = request.POST.get('population')
        description = request.POST.get('description')

        # the city object already exists, so overwrite
        # its attributes with the data from the form
        city.name = name
        city.country = country
        city.food = food
        city.population = population
        city.description = description
        # and be sure to save it!
        city.save()

        # this is new since the lecture
        # redirects back to the detail page
        # return redirect('/rio-de-janeiro')
        return redirect('/' + city.slug)

    return render(request, 'cities_app/update_city.html', {'city': city})