# Generated by Django 3.2.10 on 2024-09-25 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0018_auto_20240924_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='puntos',
            field=models.IntegerField(default=0),
        ),
    ]
