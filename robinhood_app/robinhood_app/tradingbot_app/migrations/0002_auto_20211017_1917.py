# Generated by Django 3.0.3 on 2021-10-17 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradingbot_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutinfo_crypto',
            name='asset_currency',
        ),
        migrations.RemoveField(
            model_name='aboutinfo_crypto',
            name='quote_currency',
        ),
    ]
