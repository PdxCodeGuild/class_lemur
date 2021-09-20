from django.core.management.base import BaseCommand

import requests

from pokedex.models import Pokemon, Type

class Command(BaseCommand):
    help = 'Adds Pokemon to DB'

    def handle(self, *args, **options):
        for number in range(1, 152):
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{number}')
            # print(response.json().keys())
            # dict_keys(['abilities', 'base_experience', 'forms', 'game_indices', 'height', 'held_items', 'id', 'is_default', 'location_area_encounters', 'moves', 'name', 'order', 'past_types', 'species', 'sprites', 'stats', 'types', 'weight'])
            data = response.json()

            # print(data['id'])
            # print(data['name'])
            # print(data['types'])
            # print(data['sprites']['other']['official-artwork']['front_default'])

            id = data['id']
            name = data['name']
            photo_url = data['sprites']['other']['official-artwork']['front_default']
            types = data['types']

            pokemon, created = Pokemon.objects.get_or_create(
                id=id,
                name=name,
                photo_url=photo_url
            )

            for type_dict in types:
                type_name = type_dict['type']['name']
                type, created = Type.objects.get_or_create(
                    type=type_name
                )
                pokemon.types.add(type)

            print(f'{pokemon} is in the database')

            # print(id, name, photo_url)
        