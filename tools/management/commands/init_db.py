from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.db import transaction

from enemies.models import Enemy
from hero.models import Hero, Storage, StorageRow, InventoryItem
from items.models import Item

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        with transaction.atomic():
            hero = Hero.objects.create(user=User.objects.get(username='admin'), name='Admin')
            storage = Storage.objects.create(hero=hero)

            iron_ore = Item.objects.create(
                name='Iron Ore',
                type=Item.Types.TYPE_MATERIAL,
                weight=1
            )
            iron_sword = Item.objects.create(
                name='Iron Sword',
                type=Item.Types.TYPE_EQUIPMENT,
                slot=Item.Slots.SLOT_RHAND,
                weight=2.3,
                damage=12,
                attack_delay=6,
            )
            bronze_helm = Item.objects.create(
                name='Bronze Helm',
                type=Item.Types.TYPE_EQUIPMENT,
                slot=Item.Slots.SLOT_HEAD,
                weight=3,
                armor=2,
            )
            bronze_chest = Item.objects.create(
                name='Bronze Chest',
                type=Item.Types.TYPE_EQUIPMENT,
                slot=Item.Slots.SLOT_CHEST,
                weight=6,
                armor=3,
            )

            StorageRow.objects.create(storage=storage, item=iron_ore, count=13)
            StorageRow.objects.create(storage=storage, item=iron_sword, count=1)

            InventoryItem.objects.create(hero=hero, slot=Item.Slots.SLOT_HEAD, item=bronze_helm)
            InventoryItem.objects.create(hero=hero, slot=Item.Slots.SLOT_CHEST, item=bronze_chest)

            Enemy.objects.create(
                name='Дикий кабан',
                hp=60,
                armor=1,
                attack=7,
                attack_delay=350,
            )
