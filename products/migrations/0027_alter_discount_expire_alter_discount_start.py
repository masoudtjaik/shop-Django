# Generated by Django 4.2.7 on 2024-01-15 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_product_price_discount_alter_discount_expire_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='expire',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 16, 8, 32, 35, 176975, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='discount',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 15, 8, 30, 35, 176975, tzinfo=datetime.timezone.utc)),
        ),
    ]