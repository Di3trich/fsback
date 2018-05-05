from .models import Grupo, QueHacer
from rest_framework import serializers


class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grupo
        fields = ('url', 'nombre', 'fecha')


class QueHacerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QueHacer
        fields = ('url', 'grupo', 'tarea', 'realizado')
