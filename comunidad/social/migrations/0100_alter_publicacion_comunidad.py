# Generated by Django 4.2.16 on 2024-11-27 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0099_alter_comunidad_tematica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='comunidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.comunidad'),
        ),
    ]
