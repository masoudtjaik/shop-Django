# Generated by Django 4.2.7 on 2024-01-16 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_managers_address_is_active_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OtpCode',
        ),
    ]
