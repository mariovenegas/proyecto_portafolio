# Generated by Django 4.1.2 on 2022-10-31 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='numbercontract',
            new_name='contract',
        ),
    ]
