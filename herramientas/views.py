from django.shortcuts import render

def metodos_estudio(request):
    return render(request,'metodos-estudio.html')

def calcular_promedio(request, id_estudiante):
    return render(request, "calcular-promedio.html")