# Generated by Django 4.1.2 on 2022-10-31 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_rename_numbercontract_contract_contract'),
        ('advisorys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisory',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contracts.contract'),
        ),
    ]
