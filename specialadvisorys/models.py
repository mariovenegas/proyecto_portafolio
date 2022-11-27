from django.db import models
from ssl import create_default_context
from typing_extensions import runtime
from django.db import models
from users.models import UserClient
from clients.models import Client

# Create your models here.

class Specialadvisory(models.Model):

    motive = models.CharField(max_length=200, verbose_name="Motivo de solicitud")
    description = models.CharField(max_length=500, verbose_name="Descripcion de lo sucedido")
    date = models.DateField(null=True, verbose_name="Fecha de asesoria")
    user = models.ForeignKey(UserClient, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "asesoriaespecial"
        verbose_name_plural = "asesoriasespeciales"
        ordering = [ '-created']
    
