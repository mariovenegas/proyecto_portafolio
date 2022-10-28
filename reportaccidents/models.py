from ssl import create_default_context
from typing_extensions import runtime
from django.db import models
# Create your models here.

class Reportaccident(models.Model):
    description = models.CharField(max_length=1000, verbose_name="Descripcion del accidente")
    zone = models.CharField(max_length=100, verbose_name="Area del accidente")
    date = models.DateField(null=True, verbose_name="Fecha del accidente")
    hour = models.TimeField(null=True, verbose_name="Hora del accidente")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "ReportarAccidente"
        verbose_name_plural = "ReportarAccidentes"
        ordering = [ '-created']