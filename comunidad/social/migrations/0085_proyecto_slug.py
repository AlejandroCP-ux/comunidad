# Generated by Django 4.2.16 on 2024-11-23 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0084_comunidad_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
