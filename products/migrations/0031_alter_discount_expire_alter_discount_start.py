# Generated by Django 4.2.7 on 2024-01-17 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_alter_discount_expire_alter_discount_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='expire',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 18, 8, 43, 26, 13661, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='discount',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 17, 8, 43, 26, 13661, tzinfo=datetime.timezone.utc)),
        ),
    ]