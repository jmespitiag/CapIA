from .models import Student
from django import forms
from django.forms import ValidationError, widgets
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class StudentForm(AuthenticationForm):
    class Meta:
        model = Student
        fields = ['username','password']
       
    
class StudentRegister(UserCreationForm):
    class Meta:
        model = Student
        fields = ['nombre','universitario','carrera','username']
    nombre = forms.CharField(required=True)
    universitario = forms.BooleanField(required=False)
    carrera = forms.CharField(required=False)
    
    def clean(self):
        cleaned_data = super().clean()
        universitario = cleaned_data.get('universitario', False)
        carrera = cleaned_data.get('carrera')

        if not universitario and not carrera:
            cleaned_data['carrera'] = 'N/A'

        return cleaned_data

    


        