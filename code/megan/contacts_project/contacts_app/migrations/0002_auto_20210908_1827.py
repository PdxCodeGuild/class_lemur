# Generated by Django 3.2.7 on 2021-09-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
