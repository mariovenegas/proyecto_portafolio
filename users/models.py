from ssl import create_default_context
from typing_extensions import runtime
from django.db import models
from communes.models import Commune
# Create your models here.

class User(models.Model):
    rut = models.PositiveIntegerField(verbose_name="Rut")
    dv = models.CharField(max_length=1, verbose_name="Dígito verificador")
    name = models.CharField(max_length=50, verbose_name="Nombre")
    address = models.CharField(max_length=100, verbose_name="Dirección")
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=10, verbose_name="Tipo de usuario")
    id_client = models.PositiveIntegerField(verbose_name="Identificador Cliente")
    username = models.CharField(max_length=10, verbose_name="Nombre de usuario")
    password = models.CharField(max_length=10, verbose_name="Clave de usuario")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        ordering = [ '-created']
    

