from django.db import models
from django.contrib.auth.models import User
from django.http.response import HttpResponse
import datetime

# Create your models here.
class user_posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name = 'posts')
    text = models.CharField(max_length=150)
    created_date = models.DateTimeField(null = True, blank=True)

    def __str__(self):
        return f"{self.text}\n{self.user}\n{self.created_date}"



