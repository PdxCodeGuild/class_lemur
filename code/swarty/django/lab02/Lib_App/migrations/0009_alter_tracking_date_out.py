# Generated by Django 3.2.7 on 2021-09-21 03:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lib_App', '0008_alter_tracking_date_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracking',
            name='date_out',
            field=models.DateField(default=datetime.date(2021, 9, 20), verbose_name='Date Checkout Out'),
        ),
    ]
