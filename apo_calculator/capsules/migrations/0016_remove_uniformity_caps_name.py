# Generated by Django 3.2.5 on 2022-02-17 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capsules', '0015_uniformity_production'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uniformity',
            name='caps_name',
        ),
    ]
