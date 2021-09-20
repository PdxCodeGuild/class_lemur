from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length = 50)