from django.contrib import admin
from rest_framework import serializers

from hero.models import Storage, Hero, StorageRow, HeroEquipment
from items.models import Item


class StorageRowInline(admin.TabularInline):
    model = StorageRow
    extra = 0


class HeroEquipmentInline(admin.TabularInline):
    model = HeroEquipment
    extra = 0


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    inlines = (HeroEquipmentInline,)
    readonly_fields = ('hp', 'armor', 'damage', 'weight')

    def hp(self, obj):
        return 120

    def armor(self, obj: Hero):
        return obj.armor

    def damage(self, obj: Hero):
        return obj.damage

    def weight(self, obj: Hero):
        return obj.weight


class DisplayedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'image')


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    inlines = (StorageRowInline,)
