from django import forms
from .models import Respuesta

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['Nombre_completo', 'Edad', 'categorias_ocupacionales', 'materias', 'competencia_profesionales', 'valores_ocupacionales', 'inventario_intereses']
