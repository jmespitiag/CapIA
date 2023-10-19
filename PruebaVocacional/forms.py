from .models import Test, Student
from django import forms
from django.forms import ValidationError, widgets


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = [ 'respuesta1','respuesta3','respuesta4','respuesta5','respuesta6','respuesta7','respuesta8','respuesta9','respuesta10','respuesta11','respuesta12','respuesta13','respuesta14','respuesta15','respuesta16','respuesta17','respuesta18','respuesta19','respuesta20','respuesta21','respuesta22','respuesta23','respuesta24','respuesta25','respuesta26','respuesta27','respuesta28','respuesta29','respuesta30']
        widgets ={
            'id_estudiante': forms.HiddenInput(),
            'nombre': forms.HiddenInput(),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['nombre']
    nombre = forms.CharField(required=True)