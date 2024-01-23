import random

from django.shortcuts import render
from requests import Response
from rest_framework.views import APIView


def get_raid_loot():
    pass


def add_loot_to_inventory():
    pass


# Create your views here.
class RaidView(APIView):
    def post(self, request):
        # определить героя

        # отправить в рейд
        survived = random.randint(0, 1)
        # вернуть живым с лутом
        # или мертвым без лута
        return Response({'survived': survived})
