from django.db import models

class Team(models.Model):
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f'The {self.city} {self.name}'

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='players')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    weight = models.IntegerField()
    height = models.IntegerField()
    POSITION_CHOICES = [
        ('QB', 'Quarterback'),
        ('RB', 'Running Back'),
        ('DL', 'Defensive Lineman'),
        ('WR', 'Wide Receiver'),
        ('CB', 'Cornerback'),
        ('TE', 'Tight End'),
    ]
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    bio = models.TextField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name