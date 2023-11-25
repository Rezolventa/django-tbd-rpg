from django.contrib.auth import get_user_model

from hero.models import Hero, Storage, StorageRow
from items.models import Item

User = get_user_model()


def create_test_data():
    if Item.objects.count() == 0:
        item1 = Item.objects.create(name='Ore', weight=16.6)
        item2 = Item.objects.create(name='Sword', weight=25.1)

        hero = Hero.objects.create(user=User.get(name='admin'))

        storage = Storage.objects.create(hero=hero)

        StorageRow.objects.create(storage=storage, item=item1, count=13)
        StorageRow.objects.create(storage=storage, item=item2, count=1)
