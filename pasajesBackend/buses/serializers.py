from rest_framework import serializers
from .models import Bus, Asiento, Trayecto, Horario
from usuarios.serializers import UsuarioSerializer

class TrayectoSerializer(serializers.ModelSerializer):
    modificado = serializers.DateTimeField(read_only=True)
    creado = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Trayecto
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class BusSerializer(serializers.ModelSerializer):
    modificado = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Bus
        fields = ('id', 'patente', 'chofer', 'horario', 'modificado')
    """def create(self, validated_data):
        chofer = validated_data.pop('chofer')
        horario = validated_data.pop('horario')
        bus = Bus.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user"""

class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        fields = '__all__'