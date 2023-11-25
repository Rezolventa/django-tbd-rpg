from django.urls import path
from rest_framework.routers import SimpleRouter

from trade.views import BuyItemView

router = SimpleRouter()

# router.register(r'players', PlayerEndpoint, 'players')
urlpatterns = router.urls

urlpatterns += [
    path('buy_item/', BuyItemView.as_view())
]