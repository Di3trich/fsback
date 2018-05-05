from .models import Grupo, QueHacer
from rest_framework import serializers


class QueHacerListaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QueHacer
        fields = ('url', 'tarea', 'realizado')


class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    quehacer_set = QueHacerListaSerializer(many=True, read_only=True)

    class Meta:
        model = Grupo
        fields = ('url', 'nombre', 'fecha', 'quehacer_set')


class QueHacerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QueHacer
        fields = ('url', 'grupo', 'tarea', 'realizado')
