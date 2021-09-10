from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Doggo(models.Model):

    owner = models.ForeignKey(Owner, on_delete=models.PROTECT, related_name='doggos')

    TEMPERAMENT_CHOICES = [
        ('aggresive', 'aggresive'),
        ('lazy', 'lazy'),
        ('shy', 'shy'),
        ('nervous', 'nervous'),
        ('psycho', 'psycho'),
        ('friendly', 'friendly'),
    ]

    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    weight = models.IntegerField()
    temperament = models.CharField(
        max_length=50,
        choices=TEMPERAMENT_CHOICES,
        default='friendly'
    )
    bio = models.TextField()
    photo = models.URLField()
    
    def __str__(self):
        return f"{self.name} –– {self.breed}"


"""
Doggo Fields

name
breed
weight
temperament
medical details
diet
owner

"""

