# Generated by Django 4.2.7 on 2023-11-10 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SellOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='items.item')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TradingStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('count', models.PositiveIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='items.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trade.sellorder')),
            ],
        ),
    ]
