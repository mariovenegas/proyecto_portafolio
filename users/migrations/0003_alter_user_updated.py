# Generated by Django 4.1.2 on 2022-10-22 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_comune_remove_user_region_user_commune'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización'),
        ),
    ]