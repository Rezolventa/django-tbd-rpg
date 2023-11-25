from django.contrib import admin

from trade.models import SellOrder, TradingStock


admin.site.register(SellOrder)
admin.site.register(TradingStock)
