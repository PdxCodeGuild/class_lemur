from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    favorite_artist = models.CharField(max_length=200)
    favorite_album = models.CharField(max_length=200)
    favorite_song = models.CharField(max_length=200)

    def __str__(self):
        return self.name