# Generated by Django 4.2.16 on 2024-11-03 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0064_alter_comunidad_crowuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='foto_perfil',
            field=models.ImageField(blank=True, default='/images/default-avatar.svg', null=True, upload_to='fotos_perfil'),
        ),
    ]
