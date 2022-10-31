# Generated by Django 4.1.2 on 2022-10-30 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100, verbose_name='Servicio')),
                ('description', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
                'ordering': ['-created'],
            },
        ),
    ]