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
    readonly_fields = ('hp', 'armor', 'damage', 'weight')

    def hp(self, obj):
        return 120

    def armor(self, obj: Hero):
        return obj.armor

    def damage(self, obj: Hero):
        return obj.damage

    def weight(self, obj: Hero):
        return obj.weight

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context['custom_html'] = '<h1>CUSTOM HTML HERE</h1>'
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    inlines = (StorageRowInline,)
