# Generated by Django 3.2.10 on 2024-09-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20240917_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
