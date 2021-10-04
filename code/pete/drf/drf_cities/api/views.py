from django.db.models import query
from django.shortcuts import render

from rest_framework import generics

from cities.models import City
from .serializers import CitySerializer

class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer