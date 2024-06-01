import random

from django.db import transaction
from enemies.models import Enemy
from hero.models import Hero, Storage
from items.models import Item
from raid.combat import PlayerInCombat, EnemyInCombat, CombatController


def send_to_raid(hero: Hero) -> dict:
    player = PlayerInCombat('hero', 100, 2, 12, 6)
    boar1 = EnemyInCombat(Enemy.objects.get(name='Дикий кабан'))
    boar2 = EnemyInCombat(Enemy.objects.get(name='Дикий кабан'))
    combat_controller = CombatController(player=player, enemies=[boar1, boar2])
    combat_controller.combat_result()

    if combat_controller.result == 'survived':
        raid_loot = get_raid_loot()
        add_loot_to_inventory(raid_loot, hero)
        return {'result': 'survived', 'loot': raid_loot}
    else:
        return {'result': 'dead', 'loot': None}


def get_raid_loot() -> list[dict]:
    item_count = random.randint(1, 5)
    item = Item.objects.get(name='Iron Ore')
    return [
        {
            'item_id': item.id,
            'count': item_count
        }
    ]


def add_loot_to_inventory(loot: list[dict], hero: Hero):
    with transaction.atomic():
        storage = Storage.objects.filter(hero=hero).first()
        if not storage:
            Exception('No storage found')
        for loot_row in loot:
            storage_row, created = storage.storagerow_set.get_or_create(item_id=loot_row['item_id'], defaults={'count': 0})
            storage_row.count += loot_row['count']
            storage_row.save()
            print(f'Added item_id: {loot_row["item_id"]} +{loot_row["count"]}')
