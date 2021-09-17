from django.db import models
from django.contrib.auth.models import User

class GroceryItem(models.Model):
    description = models.CharField(max_length=100)
    created_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='grocery_items')

    def __str__(self):
        return f'{self.description}; bought: {self.completed}'