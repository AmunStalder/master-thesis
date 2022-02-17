# Generated by Django 3.2.5 on 2022-02-17 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0001_initial'),
        ('capsules', '0014_remove_uniformity_production'),
    ]

    operations = [
        migrations.AddField(
            model_name='uniformity',
            name='production',
            field=models.ForeignKey(default=12345, on_delete=django.db.models.deletion.CASCADE, to='productions.productions'),
            preserve_default=False,
        ),
    ]