from django.db import models
from django.db import models
from cuentas.models import Student

# Create your models here.

class Chat(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.nombre}: {self.message}'
