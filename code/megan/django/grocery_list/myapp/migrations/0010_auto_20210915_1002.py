# Generated by Django 3.2.7 on 2021-09-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20210910_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='created_date',
            field=models.DateField(default='2021-09-15'),
        ),
    ]
