# Generated by Django 3.1.1 on 2020-10-09 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_delete_user'),
        ('restaurant', '0008_auto_20201009_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
