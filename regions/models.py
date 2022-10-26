from ssl import create_default_context
from typing_extensions import runtime
from django.db import models

# Create your models here.

class Region(models.Model):
    region = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "region"
        verbose_name_plural = "regiones"
        ordering = [ '-created']
    