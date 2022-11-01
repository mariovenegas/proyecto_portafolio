# Generated by Django 4.1.2 on 2022-11-01 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_client_updated'),
        ('users', '0003_alter_user_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id_client',
        ),
        migrations.RemoveField(
            model_name='user',
            name='type',
        ),
        migrations.AddField(
            model_name='user',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client'),
        ),
    ]