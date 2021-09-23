# Generated by Django 3.2.7 on 2021-09-20 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lib_App', '0005_alter_tracking_date_out'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracking',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='tracking',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='tracking',
            name='date_out',
            field=models.DateField(default=datetime.datetime(2021, 9, 20, 13, 21, 57, 7487), verbose_name='Date Checkout Out'),
        ),
    ]
