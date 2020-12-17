from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Hero(models.Model):
    Attribute = (
        ('Strength', 'Strength'),
        ('Agility', 'Agility'),
        ('Intelligence', 'Intelligence'),
    )
    Role = (
        ('Carry', 'Carry'),
        ('Mid', 'Mid'),
        ('Offlaner', 'Offlaner'),
        ('Soft-Support', 'Soft-Support'),
        ('Hard-Support','Hard-Support'),
    )
    Tag = (
        ('Nuker', 'Nuker'),
        ('Disabler', 'Disabler'),
        ('Jungler', 'Jungler'),
        ('Tank', 'Tank'),
        ('Escape','Escape'),
        ('Pusher','Pusher'),
        ('Initiator','Initiator'),
    )

    Skill = (
        ('Easy','Easy'),
        ('Average','Average'),
        ('Difficult','Difficult'),
    )

    name = models.CharField(max_length=20)
    atr = models.CharField(max_length=40, choices=Attribute)
    role = MultiSelectField(max_choices=5, choices=Role)
    tag = MultiSelectField(max_choices=7, choices=Tag)
    skill = models.CharField(max_length=20, choices=Skill)
    image = models.ImageField(blank=True, default='default.png')

    def __str__(self):
        return self.name

