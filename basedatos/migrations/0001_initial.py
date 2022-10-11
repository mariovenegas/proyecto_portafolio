# Generated by Django 4.1.2 on 2022-10-10 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('clave', models.CharField(max_length=10)),
                ('tipo_usuario', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
