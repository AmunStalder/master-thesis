# Generated by Django 3.2.5 on 2022-04-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('substances', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='substance',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]