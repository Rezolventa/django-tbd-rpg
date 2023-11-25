from django.contrib import admin

from hero.models import Storage, Hero, StorageRow

admin.site.register(Storage)
admin.site.register(StorageRow)
admin.site.register(Hero)
