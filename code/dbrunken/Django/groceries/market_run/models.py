from django.db import models

class Item(models.Model):
    item = models.CharField('Item', max_length=100)
    date_added = models.DateTimeField('Date added', auto_now_add=True)
    date_bought = models.DateTimeField('Date bought', blank=True, null=True)
    bought = models.BooleanField('Bought?', default=False)
    
    def __str__(self):
        return self.item