# Generated by Django 3.2.7 on 2021-09-10 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daycare', '0005_remove_doggo_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='doggo',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='daycare.owner'),
            preserve_default=False,
        ),
    ]
