from django.db import models
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    body = models.CharField(max_length=288)
    time=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts') # user.posts.all() QuerySet of all that user's posts
    archive = models.BooleanField(default=False)
    archive_date=models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return f'{self.author},{self.time},\n {self.body}'        

# {% for post in user.posts.all %}
# {{ post }}
# {% endfor %}