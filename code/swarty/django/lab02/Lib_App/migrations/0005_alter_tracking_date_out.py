# Generated by Django 3.2.7 on 2021-09-16 23:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lib_App', '0004_auto_20210916_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracking',
            name='date_out',
            field=models.DateField(default=datetime.datetime(2021, 9, 16, 16, 16, 34, 744022), verbose_name='Date Checkout Out'),
        ),
    ]
