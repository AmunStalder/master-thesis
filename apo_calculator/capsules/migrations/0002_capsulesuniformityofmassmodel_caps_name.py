# Generated by Django 3.2.5 on 2022-01-27 14:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('capsules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capsulesuniformityofmassmodel',
            name='caps_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
