# Generated by Django 4.2.16 on 2025-01-19 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0110_auto_20241216_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaña',
            name='activa',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='desafio',
            name='activada',
            field=models.BooleanField(default=True),
        ),
    ]
