from django.shortcuts import render, redirect 
from .models import Clase
from .forms import ClaseForm
from PruebaVocacional.models import Student
from datetime import time, datetime, timedelta,date

def agregar_clase(request,id_estudiante):
    estudiante = Student.objects.get(id_estudiante=id_estudiante)
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            test.id_estudiante = estudiante
            test.save()
            form.save()
            return redirect('horario',id_estudiante=id_estudiante)  
 
    else:
        form = ClaseForm()
    
    return render(request, 'agregar_clase.html', {'form': form,'id_estudiante':id_estudiante})

def horario(request, id_estudiante):
    semana = [
        'Lunes',
        'Martes',
        'Miércoles',
        'Jueves',
        'Viernes',
        'Sábado',
        'Domingo',
    ]
    


    hora_inicio = time(6, 0)
    hora_fin = time(21, 30)
    intervalo = timedelta(minutes=30)
    horas = []
    while hora_inicio <= hora_fin:
        horas.append(hora_inicio)
        hora_inicio = (datetime.combine(date.today(), hora_inicio) + intervalo).time()
    print(horas)
    
    clases = []
    for dia in semana:
        clases.append(Clase.objects.filter(id_estudiante=id_estudiante,dia=dia))
    
    print(clases)
    return render(request, 'horario.html', {'clases': clases, 'id_estudiante':id_estudiante,'semana':semana, 'horas':horas})