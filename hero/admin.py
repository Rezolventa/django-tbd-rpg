from django import forms
from django.contrib import admin
from django.db.models import Sum

from hero.models import Storage, Hero, StorageRow, InventoryItem


class StorageRowInline(admin.TabularInline):
    model = StorageRow
    extra = 0


class InventoryItemInline(admin.TabularInline):
    model = InventoryItem
    extra = 0


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    inlines = (InventoryItemInline,)
    readonly_fields = ('hp', 'armor', 'damage', 'weight')

    def hp(self, obj):
        return 120

    def armor(self, obj: Hero):
        return obj.armor

    def damage(self, obj: Hero):
        return obj.damage

    def weight(self, obj: Hero):
        return obj.weight


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    inlines = (StorageRowInline,)
