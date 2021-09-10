from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='book')
    image = models.URLField()

    def __str__(self):
        return self.title