# Generated by Django 4.1.2 on 2022-10-10 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='correo',
            new_name='email',
        ),
    ]