# Generated by Django 4.2.7 on 2024-01-13 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='national_code',
        ),
    ]