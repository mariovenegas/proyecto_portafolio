from ssl import create_default_context
from typing_extensions import runtime
from django.db import models

# Create your models here.

class User(models.Model):
    id_region = models.PositiveIntegerField(verbose_name="Identificador Region")
    region = models.CharField(max_length=1, verbose_name="Nombre")


    class Meta:
        verbose_name = "region"
        verbose_name_plural = "regiones"
        ordering = [ '-created']
    