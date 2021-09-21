from django.db import models
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    body = models.CharField(max_length=40)
    time=models.DateTimeField()
    author=models.ForeignKey(User, on_delete=models.PROTECT)
    archive = models.BooleanField(default=False)
    archive_date=models.DateTimeField(null=True)
    def __str__(self):
        return f'{self.author},{self.time},\n {self.body}'        