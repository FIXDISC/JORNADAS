from .models import Turnos
from rest_framework import serializers

class TurnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turnos
        fields = ('id','nombre', 'codigo', 'dias', 'rango')
