from .models import Grupo, QueHacer
from rest_framework import serializers


class QueHacerListaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QueHacer
        fields = ('url', 'tarea', 'realizado')


class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    quehacer_set = QueHacerListaSerializer(many=True)

    class Meta:
        model = Grupo
        fields = ('url', 'nombre', 'fecha', 'quehacer_set')

    def create(self, validated_data):
        quehacer_data = validated_data.pop('quehacer_set')
        grupo = Grupo.objects.create(**validated_data)
        for quehacer in quehacer_data:
            QueHacer.objects.create(grupo=grupo, **quehacer)
        return grupo


class QueHacerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QueHacer
        fields = ('url', 'grupo', 'tarea', 'realizado')
