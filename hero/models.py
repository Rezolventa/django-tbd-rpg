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

    def put_off(self, slot: Item.Slots):
        try:
            hero_equipment = self.heroequipment_set.get(slot=slot)
            old_item = hero_equipment.item
            hero_equipment.delete()
            return old_item
        except HeroEquipment.DoesNotExist:
            pass

    def put_on(self, item: Item):
        if self.heroequipment_set.filter(slot=item.slot).exists():
            raise Exception("Slot already in use")
        self.heroequipment_set.create(slot=item.slot, item=item)


class Storage(models.Model):
    # TODO: наследовать от новой модели Container в рамках DRY
    hero = models.OneToOneField(Hero, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.hero.name} storage'

    def add(self, item_id: int, count: int = 1):
        try:
            storage_row = self.storagerow_set.get(item_id=item_id)
            storage_row.count += count
            storage_row.save(update_fields=['count'])
        except StorageRow.DoesNotExist:
            self.storagerow_set.create(item_id=item_id, count=count)

    def remove(self, storage_row: 'StorageRow', count: int = 1) -> None:
        storage_row.count -= count
        if storage_row.count == 0:
            storage_row.delete()
        else:
            storage_row.save(update_fields=['count'])


class StorageRow(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    count = models.PositiveSmallIntegerField()
    storage = models.ForeignKey(Storage, on_delete=models.DO_NOTHING)


class HeroEquipment(models.Model):
    """
    Предметы, надетые на героя
    """
    # TODO: unique_together
    hero = models.ForeignKey(Hero, on_delete=models.DO_NOTHING)
    slot = models.CharField(choices=Item.Slots.choices, max_length=64)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)


class HeroInventory(models.Model):
    hero = models.OneToOneField(Hero, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.hero.name} inventory'

    def add(self, item_id: int, count: int = 1):
        try:
            hero_inventory_item = self.heroinventoryitem_set.get(item_id=item_id)
            hero_inventory_item.count += count
            hero_inventory_item.save(update_fields=['count'])
        except HeroInventoryItem.DoesNotExist:
            self.heroinventoryitem_set.create(item_id=item_id, count=count)

    def remove(self, hero_inventory_item: 'HeroInventoryItem', count: int = 1):
        hero_inventory_item.count -= count
        if hero_inventory_item.count == 0:
            hero_inventory_item.delete()
        else:
            hero_inventory_item.save(update_fields=['count'])


class HeroInventoryItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    count = models.PositiveSmallIntegerField()
    inventory = models.ForeignKey(HeroInventory, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.item.name} {self.count}"
