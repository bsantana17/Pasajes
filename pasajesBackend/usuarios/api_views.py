from rest_framework import viewsets
from .models import Rol, Usuario
from .serializers import RolSerializer, UsuarioSerializer
class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class PasajeroViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter(rol = 2) #Rol 2 pasajero
    serializer_class = UsuarioSerializer

class ChoferViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.filter(rol = 1) #Rol 1 chofer
    serializer_class = UsuarioSerializer
