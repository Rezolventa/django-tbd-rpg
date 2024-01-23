from django.contrib import admin

from hero.models import Storage, Hero, StorageRow, InventoryItem

admin.site.register(Storage)
admin.site.register(StorageRow)


class InventoryItemInline(admin.TabularInline):
    model = InventoryItem
    extra = 0


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    inlines = (InventoryItemInline,)
