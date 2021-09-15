from django.db import models

class GroceryItem(models.Model):
    description = models.CharField(max_length=100)
    created_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.description}; bought: {self.completed}'