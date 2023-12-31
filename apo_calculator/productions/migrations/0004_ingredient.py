# Generated by Django 3.2.5 on 2022-04-18 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('substances', '0004_rename_info_substance_infos'),
        ('productions', '0003_alter_productions_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_amount', models.FloatField()),
                ('actual_amount', models.FloatField()),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productions.productions')),
                ('substance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='substances.substance')),
            ],
            options={
                'ordering': ['substance'],
            },
        ),
    ]
