# Generated by Django 3.2.5 on 2022-04-07 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps_mass_balance', '0002_rename_relative_mass_balance_capsmassbalance_diff_mass_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='capsmassbalance',
            name='conc_per_cap_actual',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
    ]
