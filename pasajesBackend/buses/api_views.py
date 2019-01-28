from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
from usuarios.serializers import *

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    #Encontrar los asientos de un bus
    @action(detail=True)
    def asientos(self, request, *args, **kwargs):
        bus = self.get_object()
        asientos = Asiento.objects.filter(bus_id = bus.id)
        serializer = AsientoSerializer(asientos, many=True)
        return Response(serializer.data)

class AsientoViewSet(viewsets.ModelViewSet):
    queryset = Asiento.objects.all()
    serializer_class = AsientoSerializer

class TrayectoViewSet(viewsets.ModelViewSet):
    queryset = Trayecto.objects.all()
    serializer_class = TrayectoSerializer
    #Metodo para encontrar todos los horarios de un trayecto
    @action(methods=['get'], detail=True)
    def horarios(self, request, pk=None):
        trayecto = self.get_object()
        horarios = Horario.objects.filter(trayecto_id = trayecto.id)
        serializer = HorarioSerializer(horarios, many=True)
        return Response(serializer.data)
    #Metodo para encontrar todos los horarios de un trayecto sin un bus asignado
    @action(methods=['get'], detail=True)
    def sinbus(self, request, pk=None):
        trayecto = self.get_object()
        horarios = Horario.objects.filter(trayecto_id = trayecto.id)
        buses = Bus.objects.all()
        objs = []
        #Buscar horarios sin buses
        for horario in horarios:
            aux = 0
            for bus in buses:
                #Si un horario ya se encuentra en un bus no incluirlo
                if(bus.horario.id == horario.id):
                    aux = 1
            if(aux == 0):
                objs.append(horario)
            
        serializer = HorarioSerializer(objs, many=True)
        return Response(serializer.data)
    #Metodo para encontrar todos los asientos vendidos de todos los trayectos
    #Retorna una lista en el orden de los trayectos, con un contador de pasaje comprado
    @action(methods=['get'], detail=False)
    def asientos(self, request):
        trayectos = Trayecto.objects.all()
        asientosAll = []
        for trayecto in trayectos:
            busesAll = []
            contador = 0
            horarios = Horario.objects.filter(trayecto_id = trayecto.id)
            for horario in horarios:
                buses = Bus.objects.filter(horario_id = horario.id)
                for bus in buses:
                    busesAll.append(bus)
            for bus in busesAll:
                asientos = Asiento.objects.filter(bus_id = bus.id)
                for asiento in asientos:
                    if(asiento.pasajero is not None):
                        contador = contador + 1
            asientosAll.append(contador)
        return Response(asientosAll)
    #Metodo para encontrar todos los buses con su cantidad de asientos vendidos
    #Retorna una lista en el orden de los trayectos, con un contador de pasaje vendido, más la patente del bus
    @action(methods=['get'], detail=False)
    def buses(self, request):
        trayectos = Trayecto.objects.all()
        ventas = []
        indice = 0
        for trayecto in trayectos:
            busesAll = []
            contador = 0
            horarios = Horario.objects.filter(trayecto_id = trayecto.id)
            for horario in horarios:
                buses = Bus.objects.filter(horario_id = horario.id)
                for bus in buses:
                    busesAll.append(bus)
            if(len(busesAll) == 0): #Si el trayecto no tiene buses a cargo
                ventas.append(indice)
                ventas.append(0)
                ventas.append("Sin Buses")
            for bus in busesAll: #Si el trayecto tiene buses
                contador = 0
                ventas.append(indice)
                asientos = Asiento.objects.filter(bus_id = bus.id)
                for asiento in asientos:
                    if(asiento.pasajero is not None):
                        contador += 1
                ventas.append(contador)
                ventas.append(bus.patente)
            indice += 1
        return Response(ventas)

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    #Metodo para encontrar los asientos disponibles de un bus en un horario
    @action(detail=True)
    def asientos(self, request, pk=None):
        horario = self.get_object()
        bus = Bus.objects.filter(horario_id = horario.id).first()
        asientos = Asiento.objects.filter(bus_id = bus.id, pasajero = None)
        serializer = AsientoSerializer(asientos, many=True)
        return Response(serializer.data)
