from annoying.decorators import render_to
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from hero.models import StorageRow, HeroInventoryItem, Hero
from items.utils import ItemMover
from raid.utils import send_to_raid


class RaidView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        hero = request.user.hero
        result = send_to_raid(hero)
        return Response(result, status=200)


@render_to("ssss.html")
def base_view(request):
    context = {}
    return context


@render_to("hero_form/user.html")
def user_view(request):
    hero = Hero.objects.all().first()

    context = {}
    context['storage'] = StorageRow.objects.all()
    context['inventory'] = HeroInventoryItem.objects.all()
    context['equipment'] = {}
    if request.POST:
        item_mover = ItemMover(hero=hero)
        if request.POST.get('action') == 'move_to_storage':
            hero_inventory_item = HeroInventoryItem.objects.get(pk=request.POST.get('inventory_item_id'))
            move_count = int(request.POST.get('move_count'))
            item_mover.from_inventory_to_storage(hero_inventory_item, move_count)
        elif request.POST.get('action') == 'move_to_inventory':
            storage_row = StorageRow.objects.get(pk=request.POST.get('storage_row_id'))
            move_count = int(request.POST.get('move_count'))
            item_mover.from_storage_to_inventory(storage_row, move_count)
        elif request.POST.get('action') == 'activate':
            pk = request.POST.get('inventory_item_id')
            row = HeroInventoryItem.objects.get(pk=pk)
            # else:
            #     row = StorageRow.objects.get(pk=pk)
            item_mover.put_on_from_container(row)
        elif request.POST.get('action').find('put_off') != -1:
            slot = request.POST.get('action').replace('put_off_', '')
            item = hero.heroequipment_set.get(slot=slot).item
            item_mover.put_off(item)
    for equipment in hero.heroequipment_set.all():
        context['equipment'][equipment.slot] = equipment.item
    return context
