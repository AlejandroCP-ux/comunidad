# Generated by Django 4.2.16 on 2024-10-08 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0048_alter_proyecto_documentos_alter_proyecto_imagenes'),
    ]

    operations = [
        migrations.AddField(
            model_name='desafio',
            name='premio',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.premio'),
        ),
    ]