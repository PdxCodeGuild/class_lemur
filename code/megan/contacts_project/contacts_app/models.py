from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    favorite_artist = models.CharField(max_length=200)
    favorite_album = models.CharField(max_length=200)
    favorite_song = models.CharField(max_length=200)
    age = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name