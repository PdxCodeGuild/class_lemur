from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    cuisine = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name