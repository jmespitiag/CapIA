from django.db import models

class Test(models.Model):
    
    nombre = models.CharField(max_length=25)
    id = models.AutoField(primary_key=True)
    answers = models.FileField(upload_to='answers')
    
    
    def __str__(self):
        return self.nombre
    
    