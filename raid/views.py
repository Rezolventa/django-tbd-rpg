from annoying.decorators import render_to
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from hero.models import StorageRow, HeroInventoryItem
from items.models import Item
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
    context = {}
    context['storage'] = StorageRow.objects.all()
    context['inventory'] = HeroInventoryItem.objects.all()
    context['equipment'] = {}
    context['equipment']['head'] = Item.objects.get(name='Iron Helm')
    if request.POST:
        if request.POST.get('action') == 'move_to_storage':
            hero_inventory_item = HeroInventoryItem.objects.get(pk=request.POST.get('inventory_item_id'))
            StorageRow.objects.create(storage_id=4, item=hero_inventory_item.item, count=hero_inventory_item.count)
        elif request.POST.get('action') == 'move_to_inventory':
            storage_row = StorageRow.objects.get(pk=request.POST.get('storage_row_id'))
            HeroInventoryItem.objects.create(inventory_id=1, item=storage_row.item, count=storage_row.count)
    return context
