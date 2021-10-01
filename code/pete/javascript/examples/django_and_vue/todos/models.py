from django.db import models

class Todo(models.Model):
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.description} || {'completed' if self.completed else 'not completed'}"