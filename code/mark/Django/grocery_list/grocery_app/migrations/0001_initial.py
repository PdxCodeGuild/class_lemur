# Generated by Django 3.2.7 on 2021-09-08 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('complete_date', models.DateTimeField()),
                ('complete', models.BooleanField()),
            ],
        ),
    ]
