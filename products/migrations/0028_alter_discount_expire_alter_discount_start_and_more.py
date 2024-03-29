# Generated by Django 4.2.7 on 2024-01-16 05:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_alter_discount_expire_alter_discount_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='expire',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 17, 5, 47, 52, 596334, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='discount',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 16, 5, 45, 52, 596334, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='like',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_like', to='products.product'),
        ),
    ]
