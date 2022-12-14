# Generated by Django 4.1.2 on 2022-10-22 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commune', models.CharField(max_length=1, verbose_name='Comuna')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='regions.region')),
            ],
            options={
                'verbose_name': 'comuna',
                'verbose_name_plural': 'comunas',
                'ordering': ['-created'],
            },
        ),
    ]
