# Generated by Django 4.2.7 on 2024-01-14 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_discount_expire'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discount',
            name='deleted_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
