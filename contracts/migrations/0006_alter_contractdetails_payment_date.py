# Generated by Django 4.1.3 on 2022-12-02 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0005_contractdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractdetails',
            name='payment_date',
            field=models.DateField(null=True, verbose_name='Fecha de pago'),
        ),
    ]
