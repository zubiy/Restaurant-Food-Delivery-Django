# Generated by Django 3.1.1 on 2020-10-06 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180821_2311'),
        ('restaurant', '0003_auto_20201006_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='fname',
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.product'),
        ),
    ]
