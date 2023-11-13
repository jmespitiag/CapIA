from PruebaVocacional.models import Test
from cuentas.models import Student

def run():
    
    student = Student.objects.get(nombre="Susana")
    for _ in range(0,11):
        nuevo_test = Test(nombre="ExacSoc", id_estudiante=student, area_test='Ciencias exactas', area='Administrativas y contables')
        nuevo_test.save()
    