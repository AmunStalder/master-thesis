# Generated by Django 3.2.5 on 2022-07-14 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('substances', '0004_rename_info_substance_infos'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinishedMedicinalProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('main_ingredient', models.CharField(max_length=128)),
                ('manufacturer', models.CharField(max_length=128)),
                ('galenical_form', models.CharField(blank=True, choices=[('tablets', 'Tablets')], max_length=32)),
                ('dose_units_per_package', models.IntegerField()),
                ('conc_per_dose_unit_mg', models.FloatField()),
                ('price_chf', models.FloatField()),
            ],
        ),
    ]
