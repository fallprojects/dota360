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
    Team = (
        ('Radiant','Radiant'),
        ('Dire','Dire'),
    )

    name = models.CharField(max_length=20)
    atr = models.CharField(max_length=40, choices=Attribute)
    role = MultiSelectField(max_choices=5, choices=Role)
    tag = MultiSelectField(max_choices=7, choices=Tag)
    skill = models.CharField(max_length=20, choices=Skill)
    image = models.ImageField(blank=True, default='default.png')
    description = models.TextField()
    team = models.CharField(max_length=10, choices=Team)
    dotabuff = models.CharField(max_length=100)
    build = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Guide(models.Model):

    build = models.ImageField(blank=True,default='default.png')
    build2 = models.ImageField(blank=True,default='default.png')
    skillbuild = models.ImageField(blank=True,default='default.png')
    hero = models.ForeignKey(Hero,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.hero.name