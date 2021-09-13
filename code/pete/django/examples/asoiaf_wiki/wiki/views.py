from django.shortcuts import render, get_object_or_404

from .models import Character, House

def index(request):
    characters = Character.objects.order_by('house', 'name')
    return render(request, 'wiki/index.html', {'characters': characters})

def house(request, name):
    # house = House.objects.get(name=name)
    house = get_object_or_404(House, name=name)
    return render(request, 'wiki/house.html', {'house': house})