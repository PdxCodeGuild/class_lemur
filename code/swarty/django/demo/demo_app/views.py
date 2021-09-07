from django.shortcuts import render
from .models import City

def index(request):
    cities = City.objects.all()
    print(cities) # <QuerySet [<City: Portland>, <City: Rhodes>, <City: Seville>, <City: Seoul>]>
    context = {
        'cities': cities,
    }
    return render(request, 'demo_app/index.html', context)