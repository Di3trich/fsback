from django.shortcuts import render
from .models import Grupo, QueHacer


def index(request):
    grupo_lista = Grupo.objects.all()
    contexto = {'grupo_lista': grupo_lista}
    return render(request, 'que_hacer/index.html', contexto)
