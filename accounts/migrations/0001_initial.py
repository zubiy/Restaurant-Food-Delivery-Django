# Generated by Django 3.1.1 on 2020-10-05 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='no-img.jpg', upload_to='assets/images')),
                ('first_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='none@email.com', max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('birth_date', models.DateField(default='1999-12-31')),
                ('city', models.CharField(default='', max_length=255)),
                ('country', models.CharField(default='', max_length=255)),
                ('preferences', models.CharField(default='', max_length=255)),
                ('cuisine', models.CharField(default='', max_length=255)),
                ('diet', models.CharField(default='', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
