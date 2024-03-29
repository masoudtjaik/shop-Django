# Generated by Django 4.2.7 on 2024-01-19 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_alter_discount_expire_alter_discount_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='expire',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 20, 8, 42, 40, 333127, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='discount',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 19, 8, 42, 40, 333127, tzinfo=datetime.timezone.utc)),
        ),
    ]
