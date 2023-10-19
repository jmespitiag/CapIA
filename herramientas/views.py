from django.shortcuts import render, redirect 
from .models import Clase
from .forms import ClaseForm, CalculadoraNotasForm
from PruebaVocacional.models import Student
from datetime import time, datetime, timedelta,date
from .utils import calcular_promedio_ponderado

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

def metodos_estudio(request,id_estudiante):
    return render(request,'metodos-estudio.html',{'id_estudiante':id_estudiante})

def calculaNota(request, id_estudiante):
    if request.method == 'POST':
        form = CalculadoraNotasForm(request.POST)
        if form.is_valid():
            notas_creditos = []

            for i in range(1, 6):  # Supongamos que tienes 5 entradas de notas y créditos
                nota = form.cleaned_data.get(f'nota{i}')
                creditos = form.cleaned_data.get(f'creditos{i}')

                if nota is not None and creditos is not None:
                    notas_creditos.append((nota, creditos))

            promedio_ponderado = calcular_promedio_ponderado(notas_creditos)

            context = {
                'promedio_ponderado': promedio_ponderado,
                'id_estudiante': id_estudiante,  # Asegúrate de incluir id_estudiante en el contexto
            }

            return render(request, 'resultado_calculo.html', context)
    else:
        form = CalculadoraNotasForm()

    context = {
        'form': form,
        'id_estudiante': id_estudiante,  # Asegúrate de incluir id_estudiante en el contexto
    }

    return render(request, 'calcular_nota.html', context)

