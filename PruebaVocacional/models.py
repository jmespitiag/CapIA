from django.db import models

class Respuesta(models.Model):
    Nombre_completo = models.CharField(max_length=25)
    Edad = models.PositiveSmallIntegerField()
    categorias_ocupacionales = models.CharField(max_length=50)
    materias = models.CharField(max_length=50)
    competencia_profesionales = models.CharField(max_length=50)
    valores_ocupacionales =models.CharField(max_length=50)
    inventario_intereses = models.CharField(max_length=50)
    