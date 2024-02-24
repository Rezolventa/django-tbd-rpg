import random

from django.db import transaction
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from hero.models import Hero, Storage
from items.models import Item


def send_to_raid(hero: Hero) -> dict:
    survived = random.randint(0, 1) == 1
    if survived:
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
            print(f'Added item_id: {loot_row["item_id"]} - {loot_row["count"]}')


class RaidView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        hero = request.user.hero
        result = send_to_raid(hero)
        return Response(result, status=200)
