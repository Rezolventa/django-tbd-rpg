from django.urls import path
from rest_framework.routers import SimpleRouter

from trade.views import BuyItemView


app_name = 'trade'
router = SimpleRouter()
urlpatterns = router.urls

urlpatterns += [
    path('buy_item/', BuyItemView.as_view())
]
