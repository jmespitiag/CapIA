from django.db import models
from PruebaVocacional.models import Student
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

class Clase(models.Model):
    Semana = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    )

    
    id_clase = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Student, verbose_name=("ID de estudiante"), on_delete=models.CASCADE, default=00)
    nombre = models.CharField(max_length=50)
    dia = models.CharField(max_length=10, choices=Semana)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    
    
