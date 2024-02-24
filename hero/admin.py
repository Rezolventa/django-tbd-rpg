from django.contrib import admin

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


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    inlines = (StorageRowInline,)
