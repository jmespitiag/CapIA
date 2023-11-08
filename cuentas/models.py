from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):
    
    nombre = models.CharField(max_length=25)
    id_estudiante = models.AutoField(primary_key=True)
    universitario = models.BooleanField(default=False)
    carrera = models.CharField(max_length=100,default='N/A')
    

    
    def __str__(self):
        return self.nombre
    