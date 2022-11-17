from django.db import models
from ssl import create_default_context
from typing_extensions import runtime
from django.db import models
from clients.models import Client
from professionals.models import Professional
from contracts.models import Contract

# Create your models here.

class Advisory(models.Model):

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    attendees = models.CharField(max_length=200, verbose_name="Asistentes")
    topic = models.CharField(max_length=500, verbose_name="Tema de asesoria")
    date = models.DateField(null=True, verbose_name="Fecha de asesoria")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, null=True)
    state = models.CharField(max_length=10, verbose_name="Estado de la asesoría", null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "capacitacion"
        verbose_name_plural = "capacitaciones"
        ordering = [ '-created']
    
