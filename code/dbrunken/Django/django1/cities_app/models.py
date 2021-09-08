from django.db import models

# built in ORM (object relational manager)

class City(models.Model):
    name = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    population = models.IntegerField()

def __str__(self):
    return self.name    
