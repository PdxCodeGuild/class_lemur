from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    favorite_fruit = models.CharField(max_length=50)
    favorite_color = models.CharField(max_length=50)

    def __str__(self):
        return self.name