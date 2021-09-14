from django.db import models
import uuid

# Create your models here.
class Groceries(models.Model):
    item = models.CharField('Grocery Item', max_length=50)
    date_added = models.DateTimeField('Date Added', auto_now_add=True)
    date_bought = models.DateTimeField('Date Bought', editable=False, blank=True, null=True)
    cleared = models.BooleanField(default=False, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.item
