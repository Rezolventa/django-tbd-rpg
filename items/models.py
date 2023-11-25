from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='static')
    weight = models.FloatField()
