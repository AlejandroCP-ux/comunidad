# Generated by Django 4.2.16 on 2024-09-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0034_alter_desafio_max_monto_alter_desafio_min_monto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonacionComunidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('identificador_transferencia', models.CharField(max_length=50)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]