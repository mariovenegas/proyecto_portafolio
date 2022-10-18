from sqlite3 import register_converter
from ssl import create_default_context
from typing_extensions import runtime
from django.db import models

# Create your models here.
class Client(models.Model):
    rut = models.PositiveIntegerField(verbose_name="Rut")
    dv = models.CharField(max_length=1, verbose_name="Dígito verificador")
    name = models.CharField(max_length=50, verbose_name="Nombre")
    sector = models.CharField(max_length=100, verbose_name="Rubro")
    address = models.CharField(max_length=100, verbose_name="Dirección")
    comune = models.CharField(max_length=50, verbose_name="Comuna")
    region = models.CharField(max_length=50, verbose_name="Región")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = [ '-created']
    

