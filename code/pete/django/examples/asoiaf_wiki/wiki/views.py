from django.shortcuts import render, get_object_or_404

from .models import Character, House

def index(request):
    # get all objects of the Character model
    # Django ORM
    characters = Character.objects.all()
    # SQL Query
    # SELECT * FROM wiki_character

    # get all objects of the Character model who belong to House Stark
    # Djano ORM
    characters = Character.objects.filter(house_id=1)
    # SQL Query
    # SELECT * FROM wiki_character
    # WHERE house_id = 1;

    # get all objects of the Character model with Stark in the name
    # Django ORM
    Character.objects.filter(name__ends_with='Stark')
    # SQL Query
    # SELECT * FROM wiki_character
    # WHERE name LIKE '%Stark';

    characters = Character.objects.order_by('house', 'name')

    
    return render(request, 'wiki/index.html', {'characters': characters})

def house(request, name):
    # house = House.objects.get(name=name)
    house = get_object_or_404(House, name=name)
    return render(request, 'wiki/house.html', {'house': house})