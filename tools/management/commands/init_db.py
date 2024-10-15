from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.db import transaction

from enemies.models import Enemy
from hero.models import Hero, Storage, StorageRow, InventoryItem
from items.models import Item

User = get_user_model()


class Command(BaseCommand):
    def wipe_db(self):
        Enemy.objects.all().delete()
        Hero.objects.all().delete()
        InventoryItem.objects.all().delete()
        Storage.objects.all().delete()
        StorageRow.objects.all().delete()
        Item.objects.all().delete()

    def handle(self, *args, **options):
        with transaction.atomic():
            self.wipe_db()
            hero = Hero.objects.create(user=User.objects.get(username='admin'), name='Admin')
            storage = Storage.objects.create(hero=hero)

            iron_ore = Item.objects.create(
                name='Iron Ore',
                type=Item.Types.TYPE_MATERIAL,
                weight=1
            )
            StorageRow.objects.create(storage=storage, item=iron_ore, count=13)

            for weapon in self.create_weapons() + self.create_armor():
                StorageRow.objects.create(storage=storage, item=weapon, count=1)

            # InventoryItem.objects.create(hero=hero, slot=Item.Slots.SLOT_HEAD, item=bronze_helm)
            # InventoryItem.objects.create(hero=hero, slot=Item.Slots.SLOT_CHEST, item=bronze_chest)

            Enemy.objects.create(
                name='Дикий кабан',
                hp=60,
                armor=1,
                attack=7,
                attack_delay=350,
            )

    def create_weapons(self):
        iron_sword = Item.objects.create(
            name='Iron Sword',
            type=Item.Types.TYPE_EQUIPMENT,
            slot=Item.Slots.SLOT_RHAND,
            weight=2.3,
            damage=12,
            attack_delay=6,
        )

        copper_sword = Item.objects.create(
            name='Copper Sword',
            type=Item.Types.TYPE_EQUIPMENT,
            slot=Item.Slots.SLOT_RHAND,
            weight=2.2,
            damage=12,
            attack_delay=5,
        )

        bronze_sword = Item.objects.create(
            name='Bronze Sword',
            type=Item.Types.TYPE_EQUIPMENT,
            slot=Item.Slots.SLOT_RHAND,
            weight=2.1,
            damage=13,
            attack_delay=5,
        )

        iron_shield = Item.objects.create(
            name='Iron Shield',
            type=Item.Types.TYPE_EQUIPMENT,
            slot=Item.Slots.SLOT_LHAND,
            weight=4,
            armor=5,
            attack_delay=5,
        )

        return [iron_sword, copper_sword, bronze_sword, iron_shield]

    def create_armor(self):
        iron_helm = Item.objects.create(
            name='Iron Helm',
            type=Item.Types.TYPE_EQUIPMENT,
            slot=Item.Slots.SLOT_HEAD,
            weight=3.6,
            armor=2,
        )
        bronze_helm = Item.objects.create(
            name='Bronze Helm',
            type=Item.Types.TYPE_EQUIPMENT,
            slot=Item.Slots.SLOT_HEAD,
            weight=3,
            armor=2,
        )

        iron_chest = Item.objects.create(
            name='Iron Chest',
            type=Item.Types.TYPE_EQUIPMENT,
            slot=Item.Slots.SLOT_CHEST,
            weight=6,
            armor=3,
        )
        bronze_chest = Item.objects.create(
            name='Bronze Chest',
            type=Item.Types.TYPE_EQUIPMENT,
            slot=Item.Slots.SLOT_CHEST,
            weight=5.4,
            armor=4,
        )
        return [iron_helm, bronze_helm, iron_chest, bronze_chest]
