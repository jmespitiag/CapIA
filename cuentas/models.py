from django.db import models

class Student(models.Model):
    
    nombre = models.CharField(max_length=25)
    id_estudiante = models.AutoField(primary_key=True)
    universitario = models.BooleanField(default=False)
    carrera = models.CharField(max_length=100,blank=True,default=None)
    
    
    def __str__(self):
        return self.nombre
    