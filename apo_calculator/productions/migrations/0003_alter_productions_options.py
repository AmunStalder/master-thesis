# Generated by Django 3.2.5 on 2022-03-19 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0002_auto_20220217_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productions',
            options={'ordering': ['-calc_date']},
        ),
    ]
