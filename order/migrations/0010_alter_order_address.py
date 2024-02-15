# Generated by Django 5.0.1 on 2024-02-07 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_user_birthday_alter_user_is_active'),
        ('order', '0009_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='account.address'),
        ),
    ]