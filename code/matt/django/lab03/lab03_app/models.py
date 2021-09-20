from django.contrib.auth.models import User
from django.db import models


class Chirp(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='users')
    chirp = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return self.chirp


class Chirp_comments(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='users_comment')
    chirp = models.ForeignKey(
        Chirp, on_delete=models.CASCADE, related_name='comment'
    )
    comment = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
