# Generated by Django 3.2.7 on 2021-09-09 19:23

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
                ('list_title', models.CharField(max_length=40)),
                ('list_text', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
                ('comp_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
