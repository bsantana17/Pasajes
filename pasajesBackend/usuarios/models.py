from django.db import models
from django.utils import timezone

class Rol(models.Model):
    nombre = models.CharField(max_length=10)
    creado = models.DateTimeField('creado', default=timezone.now, blank=True)
    modificado = models.DateTimeField('modificado', default=timezone.now, blank=True)
    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=10)
    creado = models.DateTimeField('creado', default=timezone.now, blank=True)
    modificado = models.DateTimeField('modificado', default=timezone.now, blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    def __str__(self):
        return self.nombre + " " + self.rol.nombre