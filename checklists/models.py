from django.db import models
from clients.models import Client
from contracts.models import Contract

# Create your models here.
class Checklist(models.Model):
    description = models.CharField(max_length=500, verbose_name="Descripcion del checklist")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "checklist"
        verbose_name_plural = "checklists"
        ordering = [ '-created']

class Checklistdetail(models.Model):
    description = models.CharField(max_length=500, verbose_name="Descripcion del detalle")
    result = models.CharField(max_length=500, verbose_name="Resultado del detalle", null=True)
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", null=True)

    class Meta:
        verbose_name = "checklist detail"
        verbose_name_plural = "checklists detail"
        ordering = [ '-created']