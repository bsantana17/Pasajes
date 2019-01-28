from rest_framework import serializers
from .models import Rol, Usuario
class RolSerializer(serializers.ModelSerializer):
    modificado = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Rol
        fields = ('id','nombre', 'modificado')

class UsuarioSerializer(serializers.ModelSerializer):
    modificado = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'rol', 'modificado')