# Generated by Django 3.2.5 on 2022-05-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0008_auto_20220521_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productions',
            name='dose_units_incl_excess',
            field=models.IntegerField(null=True),
        ),
    ]
