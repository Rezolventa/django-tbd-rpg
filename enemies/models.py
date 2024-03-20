from django.db import models


class Enemy(models.Model):
    name = models.CharField(max_length=255)
    hp = models.PositiveSmallIntegerField()
    armor = models.PositiveSmallIntegerField()
    attack = models.PositiveSmallIntegerField()
    attack_delay = models.PositiveSmallIntegerField()  # сантисекунды
