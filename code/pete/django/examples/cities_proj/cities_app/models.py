from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200)
    food = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    population = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    # for models.ImageField to work, pillow needs to be installed
    photo = models.ImageField(null=True, blank=True)
    # a slug is used in the urls in place of the id or some other attribute
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name