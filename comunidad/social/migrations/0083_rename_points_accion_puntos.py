# Generated by Django 4.2.16 on 2024-11-23 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0082_rename_name_accion_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accion',
            old_name='points',
            new_name='puntos',
        ),
    ]
