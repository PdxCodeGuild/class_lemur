from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class GroceryItem(models.Model):
    list_title = models.CharField(max_length=40)
    list_text = models.CharField(max_length=200)
    creat_date = models.DateTimeField('date created')
    comp_date=models.DateTimeField('date completed')
    def __str__(self):
        return self.list_title