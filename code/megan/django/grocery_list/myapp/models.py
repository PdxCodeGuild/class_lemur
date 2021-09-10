from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    item = models.CharField(max_length=200)
    created_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    completed_date = models.DateField(null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.item
