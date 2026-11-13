from django.db import models

from django.db import models

class PermisoMunicipal(models.Model):
    comuna = models.CharField(max_length=100)
    rubro = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    institucion = models.CharField(max_length=300)
    costo = models.TextField()
    vigencia = models.CharField(max_length=200)
    enlace_oficial = models.URLField(max_length=500, blank=True, null=True)
    requisitos = models.JSONField(blank=True, null=True)
    def __str__(self):
        return self.nombre

from django.db import models

class IndicadorEconomico(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    valor = models.FloatField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - ${self.valor}"