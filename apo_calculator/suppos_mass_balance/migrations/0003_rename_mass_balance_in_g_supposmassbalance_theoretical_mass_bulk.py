# Generated by Django 3.2.5 on 2022-05-26 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppos_mass_balance', '0002_auto_20220526_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supposmassbalance',
            old_name='mass_balance_in_g',
            new_name='theoretical_mass_bulk',
        ),
    ]