from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class GroceryItem(models.Model):
    title = models.CharField(max_length=40)
    text = models.CharField(max_length=200)
    creation = models.DateTimeField('date created')
    completion=models.DateTimeField('date completed')
    completed=models.BooleanField(True)
    def __str__(self):
        return self.title