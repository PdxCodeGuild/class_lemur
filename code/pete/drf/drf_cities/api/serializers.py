from re import M
from rest_framework import serializers

from cities.models import City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__' # all fields
        # fields = ['name', 'cuisine'] # only the fields in the list/tuple