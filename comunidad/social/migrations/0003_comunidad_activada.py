# Generated by Django 3.2.10 on 2024-09-17 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20240916_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunidad',
            name='activada',
            field=models.BooleanField(default=False),
        ),
    ]
