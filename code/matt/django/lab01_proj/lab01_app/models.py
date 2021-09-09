from datetime import datetime
from django.db import models


class GroceryItem(models.Model):
    item = models.CharField(max_length=200, null=True, blank=True)
    completed = models.BooleanField(default=False, null=True)
    created_date = models.DateTimeField(
        'date published', auto_now_add=True)
    completed_date = models.DateTimeField(
        'date completed',  auto_now=True)

    def __str__(self):
        return self.item
