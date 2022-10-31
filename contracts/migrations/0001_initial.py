# Generated by Django 4.1.2 on 2022-10-30 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0003_alter_client_updated'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbercontract', models.CharField(max_length=50, verbose_name='Numero del contrato')),
                ('description', models.CharField(max_length=500, verbose_name='Descripcion del contrato')),
                ('datestart', models.CharField(max_length=100, verbose_name='Fecha de comienzo')),
                ('dateend', models.CharField(max_length=100, verbose_name='Fecha de finalizacion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.service')),
            ],
            options={
                'verbose_name': 'contrato',
                'verbose_name_plural': 'contratos',
                'ordering': ['-created'],
            },
        ),
    ]