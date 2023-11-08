from django.db import models
from cuentas.models import Student


class Test(models.Model):
    
    nombre = models.CharField(max_length=25)
    id_estudiante = models.ForeignKey(Student, verbose_name=("ID de estudiante"), on_delete=models.CASCADE)
    respuesta1 = models.IntegerField(default=00)
    respuesta2 = models.IntegerField(default=00)
    respuesta3 = models.IntegerField(default=00)
    respuesta4 = models.IntegerField(default=00)
    respuesta5 = models.IntegerField(default=00)
    respuesta6 = models.IntegerField(default=00)
    respuesta7 = models.IntegerField(default=00)
    respuesta8 = models.IntegerField(default=00)
    respuesta9 = models.IntegerField(default=00)
    respuesta10 = models.IntegerField(default=00)
    respuesta11 = models.IntegerField(default=00)
    respuesta12 = models.IntegerField(default=00)
    respuesta13  = models.IntegerField(default=00)
    respuesta14 = models.IntegerField(default=00)
    respuesta15 = models.IntegerField(default=00)
    respuesta16 = models.IntegerField(default=00)
    respuesta17 = models.IntegerField(default=00)
    respuesta18 = models.IntegerField(default=00)
    respuesta19 = models.IntegerField(default=00)
    respuesta20 = models.IntegerField(default=00)
    respuesta21 = models.IntegerField(default=00)
    respuesta22 = models.IntegerField(default=00)
    respuesta23 = models.IntegerField(default=00)
    respuesta24 = models.IntegerField(default=00)
    respuesta25 = models.IntegerField(default=00)
    respuesta26 = models.IntegerField(default=00)
    respuesta27 = models.IntegerField(default=00)
    respuesta28 = models.IntegerField(default=00)
    respuesta29 = models.IntegerField(default=00)
    respuesta30 = models.IntegerField(default=00)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.nombre
    
    

