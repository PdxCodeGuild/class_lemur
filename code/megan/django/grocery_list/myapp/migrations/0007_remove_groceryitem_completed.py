# Generated by Django 3.2.7 on 2021-09-09 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210909_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groceryitem',
            name='completed',
        ),
    ]
