from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from .models import City

# @app.index('/', methods=['GET', 'POST']) the decorator you would use if this was flask
def index(request):
    if request.method == 'POST':
        print(request.POST) # plain text from inputs
        print(request.FILES) # file uploads
        name = request.POST.get('name')
        country = request.POST.get('country')
        food = request.POST.get('food')
        population = request.POST.get('population')
        description = request.POST.get('description')
        photo = request.FILES.get('photo')
        City.objects.create(
            name=name,
            country=country,
            food=food,
            population=population,
            description=description,
            photo=photo,
            slug = slugify(name)
        )
        return redirect('/')
        
    cities = City.objects.all()
    print(cities) # <QuerySet [<City: Portland>, <City: Rhodes>, <City: Seville>, <City: Seoul>]>
    context = {
        'cities': cities,
    }
    return render(request, 'cities_app/index.html', context)

def city(request, slug): # the id comes from <int:id> in the urlpatterns in urls.py
    # city = City.objects.get(slug=slug)
    city = get_object_or_404(City, slug=slug) # prevents django from crashing if the object does not exist
    return render(request, 'cities_app/city.html', {'city': city})

def update_city(request, slug): # the id comes from <int:id> in the urlpatterns in urls.py
    city = get_object_or_404(City, slug=slug) # prevents django from crashing if the object does not exist

    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        country = request.POST.get('country')
        food = request.POST.get('food')
        population = request.POST.get('population')
        description = request.POST.get('description')

        city.name = name
        city.country = country
        city.food = food
        city.population = population
        city.description = description
        city.save()

    return render(request, 'cities_app/update_city.html', {'city': city})