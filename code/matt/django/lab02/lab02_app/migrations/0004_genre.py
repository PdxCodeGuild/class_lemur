# Generated by Django 3.2.7 on 2021-09-15 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab02_app', '0003_alter_checkout_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
                ('book', models.ManyToManyField(to='lab02_app.Book')),
            ],
        ),
    ]
