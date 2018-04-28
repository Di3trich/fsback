from django.db import models


class Grupo(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField('fecha de publicacion')

    def __str__(self):
        return self.nombre


class QueHacer(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    tarea = models.CharField(max_length=300)
    realizado = models.BooleanField(default=False)

    def __str__(self):
        return "%s [%s]" % (self.tarea, 'completado' if self.realizado else 'pendiente')
