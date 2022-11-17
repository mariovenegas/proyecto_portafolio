from django.db import models
from ssl import create_default_context
from typing_extensions import runtime
from django.db import models
from clients.models import Client
from contracts.models import Contract
from professionals.models import Professional
# Create your models here.

class Visit(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, null=True)
    reason = models.CharField(max_length=500, verbose_name="Razon de la visita")
    date = models.DateField(null=True, verbose_name="Fecha de visita")
    state = models.CharField(max_length=10, verbose_name="Estado de la asesoría", null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "visita"
        verbose_name_plural = "visitas"
        ordering = [ '-created']