# Generated by Django 4.2.7 on 2024-01-13 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_discount_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='amount',
            new_name='dis',
        ),
    ]
