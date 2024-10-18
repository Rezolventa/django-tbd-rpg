from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum

from items.models import Item

User = get_user_model()


class Hero(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='hero')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'heroes'

    @property
    def armor(self):
        result = self.inventoryitem_set.filter(item__armor__isnull=False).aggregate(total_armor=Sum('item__armor'))
        return result.get('total_armor')

    @property
    def damage(self):
        result = self.inventoryitem_set.filter(item__damage__isnull=False).aggregate(total_damage=Sum('item__damage'))
        return result.get('total_damage')

    @property
    def weight(self):
        result = self.inventoryitem_set.filter(item__weight__isnull=False).aggregate(total_weight=Sum('item__weight'))
        return result.get('total_weight')


class Storage(models.Model):
    hero = models.OneToOneField(Hero, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.hero.name} storage'


class StorageRow(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    count = models.IntegerField()
    storage = models.ForeignKey(Storage, on_delete=models.DO_NOTHING)


class HeroEquipment(models.Model):
    """
    Предметы, надетые на героя
    """
    hero = models.ForeignKey(Hero, on_delete=models.DO_NOTHING)
    slot = models.CharField(choices=Item.Slots.choices, max_length=64)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)


class HeroInventory(models.Model):
    hero = models.OneToOneField(Hero, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.hero.name} inventory'


class HeroInventoryItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    count = models.IntegerField()
    inventory = models.ForeignKey(HeroInventory, on_delete=models.DO_NOTHING)
