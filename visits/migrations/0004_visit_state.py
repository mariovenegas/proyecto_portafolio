# Generated by Django 4.1.2 on 2022-11-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0003_alter_visit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='state',
            field=models.CharField(max_length=10, null=True, verbose_name='Estado de la asesoría'),
        ),
    ]
