# Generated by Django 3.2.7 on 2021-09-16 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lib_App', '0002_alter_tracking_date_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracking',
            name='date_out',
            field=models.DateField(default=datetime.datetime(2021, 9, 16, 12, 8, 54, 420912), verbose_name='Date Checkout Out'),
        ),
    ]
