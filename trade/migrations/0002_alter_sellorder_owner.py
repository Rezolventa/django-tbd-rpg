# Generated by Django 4.2.7 on 2023-11-10 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0006_alter_hero_options_alter_storage_hero'),
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellorder',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hero.hero'),
        ),
    ]
