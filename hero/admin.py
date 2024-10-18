from django.contrib import admin
from django.template.loader import render_to_string
from rest_framework import serializers

from hero.form import HeroForm
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

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context['source'] = 'hero'
        extra_context['custom_html'] = render_to_string('admin/hero_doll_form.html')
        helms = Item.objects.filter(slot=Item.Slots.SLOT_HEAD)
        extra_context['options'] = {'helm': DisplayedItemSerializer(helms, many=True).data}
        extra_context['images'] = {'helm': DisplayedItemSerializer(helms.first()).data}
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    def add_form_data(self, extra_context: dict, helms):  # DEPRECATED
        """
        Передаёт данные в шаблон через форму.
        Пока не используется. Оставил на случай, если придётся к нему вернуться.
        """
        hero_form = HeroForm(
            options={
                'helms': {
                    'choices': [str(helm) for helm in helms],
                    'current': [str(helm) for helm in helms][0],
                },
            },
        )
        hero_form.is_valid()
        extra_context['hero_form'] = hero_form


class DisplayedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'image')


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    inlines = (StorageRowInline,)
