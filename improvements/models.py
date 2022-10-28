from sqlite3 import register_converter
from ssl import create_default_context
from typing_extensions import runtime
from django.db import models
from clients.models import Client
from professionals.models import Professional 

# Create your models here.
class Improvement(models.Model):
    case = models.CharField(max_length=500, verbose_name="Caso ")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    action = models.CharField(max_length=1000, verbose_name="Accion tomada para la mejora")
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "Mejora"
        verbose_name_plural = "Mejoras"
        ordering = [ '-created']