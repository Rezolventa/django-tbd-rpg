from django.urls import path
from rest_framework.routers import SimpleRouter

from raid.views import RaidView


app_name = 'raid'
router = SimpleRouter()

urlpatterns = router.urls

urlpatterns += [
    path('send_hero/', RaidView.as_view()),
]
