from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='authors', blank=True, null=True)
    def __str__(self):
        return self.title

class Checkout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name = 'books')
    user = models.CharField(max_length=50)
    checkout = models.BooleanField(default=False)
    timestamp = models.DateField(null = True, blank = True)
