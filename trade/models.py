from django.db import models, transaction

from hero.models import User, StorageRow, Hero
from items.models import Item


class SellOrder(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    price = models.IntegerField()
    count = models.IntegerField()
    owner = models.ForeignKey(Hero, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            # списание со склада игрока
            storage_row = StorageRow.objects.get(item=self.item, storage__hero=self.owner)
            storage_row.count -= self.count
            if storage_row.count == 0:
                storage_row.delete()
            else:
                storage_row.save()

            super().save(*args, **kwargs)

            # начисление на торговый склад
            TradingStock.objects.create(
                item=self.item,
                price=self.price,
                count=self.count,
                order=self,
            )


class TradingStock(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    order = models.ForeignKey(SellOrder, on_delete=models.DO_NOTHING)
