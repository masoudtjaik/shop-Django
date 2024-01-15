# Generated by Django 4.2.7 on 2024-01-15 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_alter_discount_expire_alter_discount_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_discount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='discount',
            name='expire',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 16, 6, 52, 48, 760570, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='discount',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 15, 6, 50, 48, 760570, tzinfo=datetime.timezone.utc)),
        ),
    ]