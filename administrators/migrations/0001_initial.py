# Generated by Django 4.1.2 on 2022-10-27 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.PositiveIntegerField(verbose_name='Rut')),
                ('dv', models.CharField(max_length=1, verbose_name='Dígito verificador')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('phone', models.PositiveIntegerField(verbose_name='Numero de telefono')),
                ('state', models.CharField(max_length=100, verbose_name='Estado de administrador')),
                ('username', models.CharField(max_length=10, verbose_name='Nombre de usuario')),
                ('password', models.CharField(max_length=10, verbose_name='Clave de usuario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Administrador',
                'verbose_name_plural': 'Administradores',
                'ordering': ['-created'],
            },
        ),
    ]
