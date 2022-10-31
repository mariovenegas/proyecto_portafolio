from django.db import models
from ssl import create_default_context
from typing_extensions import runtime
from django.db import models
from clients.models import Client
from contracts.models import Contract
from professionals.models import Professional

# Create your models here.

class Capacitation(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    attendees = models.CharField(max_length=200, verbose_name="Asistentes")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=500, verbose_name="Tema de capacitacion")
    date = models.CharField(max_length=100, verbose_name="Fecha de capacitacion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "capacitacion"
        verbose_name_plural = "capacitaciones"
        ordering = [ '-created']
    