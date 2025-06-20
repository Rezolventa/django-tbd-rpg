from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    # swagger
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('admin/', admin.site.urls),
    path('api/', include('trade.urls', namespace='trade')),
    path('api/', include('raid.urls', namespace='raid')),
    path('api/websocket/', include('websocket.urls', namespace='websocket')),
]

# raid/send_hero
# ...
