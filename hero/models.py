from django.contrib.auth import get_user_model
from django.db import models
from items.models import Item

User = get_user_model()


class Hero(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'heroes'


class Storage(models.Model):
    hero = models.OneToOneField(Hero, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.hero.name} storage'


class StorageRow(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    count = models.IntegerField()
    storage = models.ForeignKey(Storage, on_delete=models.DO_NOTHING)


class InventoryItem(models.Model):
    """
    Предметы, надетые на героя
    """
    hero = models.ForeignKey(Hero, on_delete=models.DO_NOTHING)
    slot = models.CharField(choices=Item.Slots.choices, max_length=64)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)

    # TODO: slot validation on save