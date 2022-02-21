# Generated by Django 3.2.5 on 2022-02-21 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0002_auto_20220217_1740'),
        ('capsules', '0016_remove_uniformity_caps_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uniformity',
            name='id',
        ),
        migrations.AlterField(
            model_name='uniformity',
            name='production',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='productions.productions'),
        ),
    ]