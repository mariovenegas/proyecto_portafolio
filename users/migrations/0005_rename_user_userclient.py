# Generated by Django 4.1.2 on 2022-11-01 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communes', '0003_alter_commune_commune'),
        ('clients', '0003_alter_client_updated'),
        ('users', '0004_remove_user_id_client_remove_user_type_user_client'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserClient',
        ),
    ]
