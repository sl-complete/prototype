# Generated by Django 4.2.16 on 2025-02-17 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0003_remove_band_band_name_remove_band_band_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='tier',
        ),
    ]
