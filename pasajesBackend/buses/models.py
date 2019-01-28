from django.db import models
from django.utils import timezone
from usuarios.models import Usuario

class Trayecto(models.Model):
    origen = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    creado = models.DateTimeField('creado', default=timezone.now, blank=True)
    modificado = models.DateTimeField('modificado', default=timezone.now, blank=True)
    def __str__(self):
        return "Desde: " + self.origen + " Hacia: " + self.destino

class Horario(models.Model):
    trayecto = models.ForeignKey(Trayecto, on_delete=models.PROTECT, blank = True, null=True)
    partida = models.DateTimeField('partida')
    llegada = models.DateTimeField('llegada')
    def __str__(self):
        return "Partida: " + str(self.partida) + " Llegada: " + str(self.llegada)

class Bus(models.Model):
    patente = models.CharField(max_length=10)
    chofer = models.ForeignKey(Usuario, on_delete=models.PROTECT, blank = True, null=True)
    horario = models.ForeignKey(Horario, on_delete=models.PROTECT, blank = True, null=True)
    creado = models.DateTimeField('creado', default=timezone.now, blank=True)
    modificado = models.DateTimeField('modificado', default=timezone.now, blank=True)
    def save(self, *args, **kwargs):
        super(Bus, self).save(*args, **kwargs)
        for x in range(1, 11):
            asiento = Asiento(numero = x, bus = self)
            asiento.save()


class Asiento(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Usuario, on_delete=models.PROTECT, blank = True, null=True)
    numero = models.IntegerField(default=0)
    def __str__(self):
        return "Asiento " + str(self.numero) + " del bus: " + self.bus.patente


