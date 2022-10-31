from django.db import models
from ssl import create_default_context
from typing_extensions import runtime
from django.db import models
from clients.models import Client
from services.models import Service
# Create your models here.

class Contract(models.Model):
    contract = models.CharField(max_length=50, verbose_name="Numero del contrato")
    description = models.CharField(max_length=500, verbose_name="Descripcion del contrato")
    datestart = models.CharField(max_length=100, verbose_name="Fecha de comienzo")
    dateend = models.CharField(max_length=100, verbose_name="Fecha de finalizacion")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "contrato"
        verbose_name_plural = "contratos"
        ordering = [ '-created']
    