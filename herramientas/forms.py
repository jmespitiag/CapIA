from django import forms
from .models import Clase

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['nombre', 'dia', 'hora_inicio','hora_fin']
        widgets = {
            'id_estudiante': forms.HiddenInput(),
            
            'hora_inicio' : forms.TimeInput(
                attrs={'type': 'time','step': '1800','min': '06:00', 'max': '22:00'}),
            
            'hora_fin': forms.TimeInput(
                attrs={'type': 'time','step': '1800','min': '06:00', 'max': '22:00'}),
        }
        