from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateField()
    author = models.CharField(max_length=50)
    def __str__(self):
        return self.title


class Author(models.Model):
    author = models.ForeignKey(Book, on_delete=models.PROTECT, related_name ='authors')
    def __str__(self):
        return self.author