from django.db import models

# Create your models here.
class Groceries(models.Model):
    item = models.CharField('Grocery Item', max_length=50)
    date_added = models.DateTimeField('Date Added', auto_now_add=True)
    date_bought = models.DateTimeField('Date Bought', editable=False, blank=True, null=True)
    cleared = models.BooleanField('Was Purchased', default=False)
    
    def __str__(self):
        return self.item
