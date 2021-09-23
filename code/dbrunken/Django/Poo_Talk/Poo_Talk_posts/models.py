from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class Post(models.Model):
    text = models.CharField(max_length=256)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField()

    def __str__(self):
        return f'{self.created_by}; {self.created_date}; {self.text}'
