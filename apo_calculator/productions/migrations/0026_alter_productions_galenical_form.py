# Generated by Django 3.2.5 on 2022-07-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0025_alter_ingredient_required_amount_of_tabs_incl_excess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productions',
            name='galenical_form',
            field=models.CharField(choices=[('capsules', 'Capsules'), ('suppositories', 'Suppositories')], max_length=16),
        ),
    ]
