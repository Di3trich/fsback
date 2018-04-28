from django.shortcuts import render
from .models import Grupo, QueHacer
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    grupo_lista = Grupo.objects.all()
    contexto = {'grupo_lista': grupo_lista}
    return render(request, 'que_hacer/index.html', contexto)


def registro(request, grupo_id):
    if request.POST['tarea'] == '':
        return HttpResponseRedirect(reverse('que_hacer:index'))
    grupo = Grupo.objects.get(pk=grupo_id)
    grupo.quehacer_set.create(tarea=request.POST['tarea'])
    return HttpResponseRedirect(reverse('que_hacer:index'))


def realizado(request, quehacer_id):
    queHacer = QueHacer.objects.get(pk=quehacer_id)
    queHacer.realizado = not queHacer.realizado
    queHacer.save()
    return HttpResponseRedirect(reverse('que_hacer:index'))
