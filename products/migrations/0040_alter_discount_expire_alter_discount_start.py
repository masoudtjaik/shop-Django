# Generated by Django 5.0.1 on 2024-01-23 08:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0039_alter_category_image_alter_discount_expire_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='expire',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 9, 1, 11, 50999, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='discount',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 23, 9, 1, 11, 50999, tzinfo=datetime.timezone.utc)),
        ),
    ]
