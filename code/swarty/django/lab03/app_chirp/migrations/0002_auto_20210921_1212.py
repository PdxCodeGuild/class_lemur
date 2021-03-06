# Generated by Django 3.2.7 on 2021-09-21 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_chirp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='archive_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 9, 21, 12, 12, 45, 21812)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(max_length=288),
        ),
    ]
