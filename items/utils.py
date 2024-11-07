from django.db.transaction import atomic

from hero.models import HeroInventoryRow, StorageRow, HeroEquipment, Storage, HeroInventory
from items.models import Item


class ItemMover:
    def __init__(self, hero):
        self.hero = hero
        self.inventory = self.hero.heroinventory
        self.storage = self.hero.storage

    def from_inventory_to_storage(self, hero_inventory_row: HeroInventoryRow, move_count: int) -> None:
        with atomic():
            hero_inventory_row.inventory.remove(hero_inventory_row, move_count)
            self.storage.add(hero_inventory_row.item_id, move_count)

    def from_storage_to_inventory(self, storage_row: StorageRow, move_count: int) -> None:
        with atomic():
            storage_row.storage.remove(storage_row, move_count)
            self.inventory.add(storage_row.item_id, move_count)

    def put_on_from_container(self, container_row: StorageRow | HeroInventoryRow):
        with atomic():
            old_item = self.hero.put_off(container_row.item.slot)

            if old_item:
                self.inventory.add(old_item.id)
            self.hero.put_on(container_row.item)

            container = self.storage if container_row is StorageRow else self.inventory
            container.remove(container_row)

    def put_off(self, item: Item):
        with atomic():
            self.hero.put_off(item.slot)
            self.inventory.add(item.id)
