from django.db import models

# Create your models here.
class Turnos(models.Model):
    list_display = ('id', 'codigo', 'nombre', 'dias', 'rango')

    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=5,default='')
    dias = models.CharField(max_length=200)
    rango = models.CharField(max_length=200)

    def __str__(self):
        return str(self.pk)+" | "+self.codigo+" | "+self.nombre+" | "+self.dias+" | "+self.rango
