from ssl import create_default_context
from typing_extensions import runtime
from django.db import models

# Create your models here.

class User(models.Model):
    id_commune = models.PositiveIntegerField(verbose_name="Identificador comuna")
    commune = models.CharField(max_length=1, verbose_name="Comuna")


    class Meta:
        verbose_name = "comuna"
        verbose_name_plural = "comunas"
        ordering = [ '-created']
    