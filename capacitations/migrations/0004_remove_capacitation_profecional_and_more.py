# Generated by Django 4.1.2 on 2022-10-27 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capacitations', '0003_alter_capacitation_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capacitation',
            name='profecional',
        ),
        migrations.AddField(
            model_name='capacitation',
            name='professional',
            field=models.CharField(max_length=20, null=True, verbose_name='Profesional'),
        ),
    ]
