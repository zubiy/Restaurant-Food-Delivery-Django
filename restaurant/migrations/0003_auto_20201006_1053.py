# Generated by Django 3.1.1 on 2020-10-06 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0002_customer_item_menu_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
