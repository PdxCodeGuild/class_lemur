# Generated by Django 3.2.7 on 2021-09-21 03:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lib_App', '0006_auto_20210920_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracking',
            name='date_out',
            field=models.DateField(default=datetime.datetime(2021, 9, 20, 20, 14, 15, 846053), verbose_name='Date Checkout Out'),
        ),
    ]
