# Generated by Django 3.2.10 on 2024-09-22 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0009_terminoscondiciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='seguidos',
            field=models.ManyToManyField(blank=True, to='social.PerfilUsuario'),
        ),
    ]