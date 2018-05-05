from django.shortcuts import render
from .models import Grupo, QueHacer
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from .serializers import GrupoSerializer, QueHacerSerializer


def index(request):
    grupo_lista = Grupo.objects.all()
    contexto = {'grupo_lista': grupo_lista}
    return render(request, 'que_hacer/index.html', contexto)


def registro(request, grupo_id):
    if request.POST['tarea'] == '':
        return HttpResponseRedirect(reverse('index'))
    grupo = Grupo.objects.get(pk=grupo_id)
    grupo.quehacer_set.create(tarea=request.POST['tarea'])
    return HttpResponseRedirect(reverse('index'))


def realizado(request, quehacer_id):
    queHacer = QueHacer.objects.get(pk=quehacer_id)
    queHacer.realizado = not queHacer.realizado
    queHacer.save()
    return HttpResponseRedirect(reverse('index'))


def eliminar(request, quehacer_id):
    queHacer = QueHacer.objects.get(pk=quehacer_id)
    queHacer.delete()
    return HttpResponseRedirect(reverse('index'))


class GrupoViewSet(viewsets.ModelViewSet):
    """
    API para crear, editar y eliminar Grupos
    """
    queryset = Grupo.objects.all().order_by('-fecha')
    serializer_class = GrupoSerializer


class QueHacerViewSet(viewsets.ModelViewSet):
    """
    API para crear, editar y eliminar QueHacer
    """
    queryset = QueHacer.objects.all()
    serializer_class = QueHacerSerializer
