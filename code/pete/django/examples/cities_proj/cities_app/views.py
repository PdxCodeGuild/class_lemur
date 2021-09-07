from django.shortcuts import render, redirect
from .models import City

def index(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        country = request.POST.get('country')
        food = request.POST.get('food')
        population = request.POST.get('population')
        City.objects.create(
            name=name,
            country=country,
            food=food,
            population=population
        )
        return redirect('/')
        
    cities = City.objects.all()
    print(cities) # <QuerySet [<City: Portland>, <City: Rhodes>, <City: Seville>, <City: Seoul>]>
    context = {
        'cities': cities,
    }
    return render(request, 'cities_app/index.html', context)
