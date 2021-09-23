from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    description = models.CharField(max_length=100, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    complete_date = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField(null=False)

    def __str__(self):
        return self.description