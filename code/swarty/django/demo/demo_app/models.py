from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    population = models.IntegerField()
