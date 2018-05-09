from .models import Grupo, QueHacer
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist


class QueHacerListaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(label='id', read_only=False, required=False)

    class Meta:
        model = QueHacer
        fields = ('url', 'id', 'tarea', 'realizado')


class GrupoSerializer(serializers.HyperlinkedModelSerializer):
    quehacer_set = QueHacerListaSerializer(many=True)

    class Meta:
        model = Grupo
        fields = ('url', 'nombre', 'fecha', 'quehacer_set')

    def create(self, validated_data):
        quehacer_data = validated_data.pop('quehacer_set')
        grupo = Grupo.objects.create(**validated_data)
        for quehacer in quehacer_data:
            grupo.quehacer_set.create(**quehacer)
        return grupo

    def update(self, instance, validated_data):
        quehacer_data = validated_data.pop('quehacer_set')
        instance.nombre = validated_data.get('nombre')
        instance.fecha = validated_data.get('fecha')
        instance.save()
        for quehacer in quehacer_data:
            id = quehacer.pop('id', None)
            if id is None:
                instance.quehacer_set.create(**quehacer)
            else:
                try:
                    quehacer_instance = QueHacer.objects.get(pk=id)
                    quehacer_instance.grupo = instance
                    quehacer_instance.tarea = quehacer.get('tarea')
                    quehacer_instance.realizado = quehacer.get('realizado')
                    quehacer_instance.save()
                except ObjectDoesNotExist:
                    instance.quehacer_set.create(**quehacer)
        return instance


class QueHacerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QueHacer
        fields = ('url', 'grupo', 'tarea', 'realizado')
