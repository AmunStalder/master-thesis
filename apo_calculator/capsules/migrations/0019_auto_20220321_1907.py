# Generated by Django 3.2.5 on 2022-03-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capsules', '0018_auto_20220321_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniformity',
            name='mass_20_caps_full',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='uniformity',
            name='mass_max1',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='uniformity',
            name='mass_max2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='uniformity',
            name='mass_max3',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='uniformity',
            name='mass_min1',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='uniformity',
            name='mass_min2',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='uniformity',
            name='mass_min3',
            field=models.FloatField(),
        ),
    ]
