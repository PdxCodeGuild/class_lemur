# Generated by Django 3.2.7 on 2021-09-09 19:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groceries',
            fields=[
                ('item', models.CharField(max_length=50, verbose_name='Grocery Item')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Added')),
                ('cleared', models.BooleanField(verbose_name='Added?')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
