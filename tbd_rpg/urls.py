from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('swagger/', TemplateView.as_view(
        template_name='swagger.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger'),
    path('openapi', get_schema_view(
        title="Here should be a title",
        description="Here should be a description",
        version="1.0",
        # permission_classes=(AllowAny,),
        # public=True,
    ), name='openapi-schema'),
    path('admin/', admin.site.urls),
    path('trade/', include(('trade.urls', 'trade'), namespace='trade')),
]
