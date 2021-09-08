from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    population = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name