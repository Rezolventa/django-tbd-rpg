from django.db import models


class Item(models.Model):
    class Slots(models.TextChoices):
        SLOT_HEAD = 'head', 'head'
        SLOT_CHEST = 'chest', 'chest'
        SLOT_ARMS = 'arms', 'arms'
        SLOT_LEGS = 'legs', 'legs'
        SLOT_FEET = 'feet', 'feet'
        SLOT_RHAND = 'rhand', 'right hand'
        SLOT_LHAND = 'lhand', 'left hand'
        SLOT_BACKPACK = 'backpack', 'backpack'

    class Types(models.TextChoices):
        TYPE_EQUIPMENT = 'equipment', 'equipment'
        TYPE_MATERIAL = 'material', 'material'

    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='static')
    type = models.CharField(choices=Types.choices, max_length=64)
    slot = models.CharField(choices=Slots.choices, max_length=64)
    weight = models.FloatField()

    def __str__(self):
        return f'{self.pk} {self.name}'
