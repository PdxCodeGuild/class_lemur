# Generated by Django 3.2.7 on 2021-10-05 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
