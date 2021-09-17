# Generated by Django 3.2.7 on 2021-09-16 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('position', models.CharField(choices=[('QB', 'Quarterback'), ('RB', 'Running Back'), ('DL', 'Defensive Lineman'), ('WR', 'Wide Receiver'), ('CB', 'Cornerback')], max_length=2)),
                ('bio', models.TextField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='players', to='nfl.team')),
            ],
        ),
    ]