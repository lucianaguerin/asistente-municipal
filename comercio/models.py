from django.db import models

class PermisoMunicipal(models.Model):
    nombre = models.CharField(max_length=255)
    comuna = models.CharField(max_length=120)
    rubro = models.CharField(max_length=200)
    costo = models.CharField(max_length=255)
    vigencia = models.CharField(max_length=200)
    institucion = models.CharField(max_length=255)
    oficina_responsable = models.CharField(max_length=255)
    requisitos_paso_a_paso = models.TextField()
    enlace = models.URLField(max_length=255)

    def __str__(self):
        return self.nombre