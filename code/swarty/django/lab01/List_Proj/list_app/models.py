from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class GroceryItem(models.Model):
    title = models.CharField(max_length=40)
    creation = models.DateTimeField('date created', auto_now_add=True)
    completion=models.DateTimeField('date completed', null=True, blank=True)
    completed=models.BooleanField(default=False)
    def __str__(self):
        return self.title