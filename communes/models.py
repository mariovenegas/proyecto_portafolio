from email.policy import default
from ssl import create_default_context
from typing_extensions import runtime
from django.db import models
from regions.models import Region

# Create your models here.

class Commune(models.Model):
    commune = models.CharField(max_length=100, verbose_name="Comuna")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "comuna"
        verbose_name_plural = "comunas"
        ordering = [ '-created']
    