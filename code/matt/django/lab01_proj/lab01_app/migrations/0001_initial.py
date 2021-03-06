# Generated by Django 3.2.7 on 2021-09-08 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(verbose_name='date published')),
                ('completed_date', models.DateTimeField(verbose_name='date completed')),
            ],
        ),
    ]
