from django.db import models

class Pokemon(models.Model):
    class Meta:
        verbose_name_plural = 'pokemon'

    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    photo_url = models.URLField()
    types = models.ManyToManyField('Type')

    def __str__(self):
        return self.name.title()

class Type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type