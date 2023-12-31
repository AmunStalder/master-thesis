# Generated by Django 3.2.5 on 2022-07-17 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('substances', '0005_finishedmedicinalproduct'),
        ('productions', '0019_alter_ambvvalue_roa'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='fmp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='substances.finishedmedicinalproduct'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='substance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='substances.substance'),
        ),
    ]
