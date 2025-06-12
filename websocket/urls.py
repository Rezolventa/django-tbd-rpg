from django.urls import path
from rest_framework.routers import DefaultRouter

from websocket.views import ws_debug

app_name = "ws"
api_router = DefaultRouter()

urlpatterns = [
    path('ws-debug/', ws_debug),
]

urlpatterns += api_router.urls
