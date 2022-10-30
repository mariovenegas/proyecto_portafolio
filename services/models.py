from ssl import create_default_context
from typing_extensions import runtime
from django.db import models

# Create your models here.

class Service(models.Model):
    service = models.CharField(max_length=100, verbose_name="Servicio")
    description = models.CharField(max_length=100, verbose_name="Descripcion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = [ '-created']
