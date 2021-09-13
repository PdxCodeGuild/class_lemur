from django.db import models

class House(models.Model):
    name = models.CharField(max_length=50)
    words = models.CharField(max_length=150)
    sigil_photo = models.URLField()
    sigil_description = models.CharField(max_length=150)

    # castle = models.ForeignKey('Location', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return 'House ' + self.name

class Character(models.Model):
    house = models.ForeignKey(House, on_delete=models.PROTECT, related_name='characters')
    name = models.CharField(max_length=100)

    locations_visited = models.ManyToManyField('Location', 'characters')

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name