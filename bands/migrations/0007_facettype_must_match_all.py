# Generated by Django 4.2.16 on 2025-02-17 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0006_remove_band_currency_code_remove_band_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='facettype',
            name='must_match_all',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
