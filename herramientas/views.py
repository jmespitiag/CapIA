from django.shortcuts import render, redirect 
from .models import Clase, Nota
from .forms import ClaseForm, CalculadoraNotasForm
from PruebaVocacional.models import Student
from datetime import time, datetime, timedelta,date
from django.http import JsonResponse

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

def calcular_promedio(request, id_estudiante):
    if request.method == 'POST':
        student = Student.objects.get(id_estudiante=id_estudiante)
        notas_antiguas = Nota.objects.filter(student=student)
        notas_antiguas.delete()
        materias = request.POST.getlist("materia[]")
        notas = request.POST.getlist("nota[]")
        creditos = request.POST.getlist("creditos[]")
        for materia, nota, credito in zip(materias, notas, creditos):
            nota_agregar = Nota(student=student, nombre=materia, nota=nota, creditos=credito)
            nota_agregar.save()
        print(Nota.objects.filter(student=student))
        promedio = promedio_ponderado(notas, creditos)
        return JsonResponse({"promedio":promedio})
    return render(request, 'calcular-promedio.html', {'id_estudiante':id_estudiante})

def promedio_ponderado(calificaciones:list, creditos:list):
    calificaciones = [float(calificacion) for calificacion in calificaciones]
    creditos = [float(credito) for credito in creditos]
    productos = [calificacion * credito for calificacion, credito in zip(calificaciones, creditos)]
    suma_productos = sum(productos)
    suma_creditos = sum(creditos)
    promedio_ponderado = suma_productos / suma_creditos

    return promedio_ponderado