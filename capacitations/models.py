from django.db import models
from ssl import create_default_context
from typing_extensions import runtime
from django.db import models

# Create your models here.

class Capacitation(models.Model):
    attendees = models.CharField(max_length=200, verbose_name="Asistentes")
    profecional = models.CharField(max_length=20, verbose_name="Profesional")
    topic = models.CharField(max_length=500, verbose_name="Tema de capacitacion")
    date = models.CharField(max_length=100, verbose_name="Fecha de capacitacion")
    id_client = models.CharField(max_length=50, verbose_name="Identificador cliente")
    id_contract = models.CharField(max_length=50, verbose_name="Identificador contrato")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "capacitacion"
        verbose_name_plural = "capacitaciones"
        ordering = [ '-created']
    