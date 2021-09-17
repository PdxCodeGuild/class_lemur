from django.shortcuts import render, get_object_or_404
# from django.views import generic

from .models import Character, House

def index(request):
    # # get all objects of the Character model
    # # Django ORM
    # characters = Character.objects.all()
    # # SQL Query
    # # SELECT * FROM wiki_character

    # # get all objects of the Character model who belong to House Stark
    # # Djano ORM
    # characters = Character.objects.filter(house_id=1)
    # # SQL Query
    # # SELECT * FROM wiki_character
    # # WHERE house_id = 1;

    # # get all objects of the Character model with Stark in the name
    # # Django ORM
    # characters = Character.objects.filter(name__ends_with='Stark')
    # # SQL Query
    # # SELECT * FROM wiki_character
    # # WHERE name LIKE '%Stark';

    characters = Character.objects.order_by('house', 'name')

    
    return render(request, 'wiki/index.html', {'characters': characters})

def house(request, name):
    # house = House.objects.get(name=name)
    house = get_object_or_404(House, name=name)
    return render(request, 'wiki/house.html', {'house': house})

# class IndexView(generic.ListView):
#     # model = Character
#     template_name = 'wiki/index.html'
#     context_object_name = 'characters'

#     def get_queryset(self):
#         return Character.objects.order_by('house', 'name')

        

# class HouseView(generic.DetailView):
#     model = House
#     template_name = 'wiki/house.html'

    