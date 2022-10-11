from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=20)
    clave = models.CharField(max_length=10)
    tipo_usuario = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)