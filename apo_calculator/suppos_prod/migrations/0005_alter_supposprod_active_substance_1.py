# Generated by Django 3.2.5 on 2022-05-11 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0007_alter_ingredient_price_per_amount'),
        ('suppos_prod', '0004_auto_20220408_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supposprod',
            name='active_substance_1',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='productions.ingredient'),
        ),
    ]
