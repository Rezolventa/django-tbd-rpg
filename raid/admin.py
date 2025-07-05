from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.urls import reverse

from raid.models import Location


def send_to_raid():
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    change_form_template = 'admin/raid/location/change_form.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'send-to-raid/<int:location_id>/',
                self.admin_site.admin_view(self.send_to_raid_view),
                name='location-send-to-raid',
            ),
        ]
        return custom_urls + urls

    def send_to_raid_view(self, request, location_id):
        location = self.get_object(request, location_id)
        if location:
            send_to_raid()
        return HttpResponseRedirect(reverse(
            f'admin:raid_location_change',
            args=[location_id],
        ))

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_send_to_raid'] = True
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    # def change_form_template(self):
    #     return 'admin/raid/location/change_form.html'