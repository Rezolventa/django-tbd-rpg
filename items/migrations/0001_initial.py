# Generated by Django 4.2.7 on 2024-01-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to='static')),
                ('type', models.CharField(choices=[('equipment', 'equipment'), ('material', 'material')], max_length=64)),
                ('slot', models.CharField(choices=[('head', 'head'), ('chest', 'chest'), ('arms', 'arms'), ('legs', 'legs'), ('feet', 'feet'), ('rhand', 'right hand'), ('lhand', 'left hand'), ('backpack', 'backpack')], max_length=64)),
                ('weight', models.FloatField()),
            ],
        ),
    ]