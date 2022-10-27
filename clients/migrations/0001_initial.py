# Generated by Django 4.1.2 on 2022-10-18 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.PositiveIntegerField(verbose_name='Rut')),
                ('dv', models.CharField(max_length=1, verbose_name='Dígito verificador')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('sector', models.CharField(max_length=100, verbose_name='Rubro')),
                ('address', models.CharField(max_length=100, verbose_name='Dirección')),
                ('comune', models.CharField(max_length=50, verbose_name='Comuna')),
                ('region', models.CharField(max_length=50, verbose_name='Región')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
                'ordering': ['-created'],
            },
        ),
    ]