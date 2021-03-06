# Generated by Django 3.0.3 on 2021-10-13 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutInfo_Crypto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_currency', models.CharField(max_length=200)),
                ('display_only', models.CharField(max_length=200)),
                ('max_order_size', models.CharField(max_length=200)),
                ('min_order_size', models.CharField(max_length=200)),
                ('min_order_price_increment', models.CharField(max_length=200)),
                ('min_order_quantity_increment', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('quote_currency', models.CharField(max_length=200)),
                ('symbol', models.CharField(max_length=200)),
                ('tradability', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='historical_Crypto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begins_at', models.CharField(max_length=200)),
                ('open_price', models.DateTimeField(verbose_name='date published')),
                ('close_price', models.CharField(max_length=200)),
                ('high_price', models.CharField(max_length=200)),
                ('low_price', models.CharField(max_length=200)),
                ('volume', models.CharField(max_length=200)),
                ('session', models.CharField(max_length=200)),
                ('interpolated', models.CharField(max_length=200)),
                ('symbol', models.CharField(max_length=200)),
            ],
        ),
    ]
