from django.db import models

# Create your models here.
class Book(models.Model):
    checked = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    FICTION = 'fiction'
    NON_FICTION = 'non-fiction'
    BOOK_TYPES = [
        (FICTION, 'fiction'),
        (NON_FICTION, 'non-fiction')
    ]
    book_type = models.CharField(max_length=50, choices=BOOK_TYPES, default=FICTION)
    
    def __str__(self):
        return self.title
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.last_name
    
class Checkout(models.Model):
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
    user = models.CharField('User', max_length=250, null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    checkout = models.BooleanField('Checked In/Out', default=False)
    