from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Test, Student
from .forms import TestForm, StudentForm



def home(request,id_estudiante):
    
    return render(request,'home.html',{'id_estudiante': id_estudiante})

def home_name(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            estudiante = form.save()  
            return redirect('home', id_estudiante=estudiante.id_estudiante)
    else:
        form = StudentForm()
    return render(request, 'home_name.html', {'form': form})
        
        
        
        
        


def test(request,id_estudiante):
    return render(request,'test.html',{'id_estudiante': id_estudiante})

def answers(request,id_estudiante):
    
    student = Student.objects.get(id_estudiante=id_estudiante)
    print(student.nombre)
    print(student.id_estudiante)
    form = TestForm(initial={'nombre': student.nombre, 'id_estudiante':student.id_estudiante})
    questions =['¿Te gusta trabajar con números y fórmulas?','¿Te gustaría trabajar en un laboratorio?','¿Te sientes atraído/a por el mundo de los negocios?','¿Te gusta leer y analizar obras literarias?','¿Te gustaría trabajar en un hospital?','¿Te atrae la idea de diseñar edificios y construcciones?','¿Te gusta crear contenido para redes sociales?','¿Te atrae la idea de investigar nuevos medicamentos?','¿Te interesa la programación de computadoras?','¿Te gustaría trabajar en laindustria cinematográfica?','¿Te sientes atraído/a por el arte y la creatividad?','¿Te gustaría trabajar en una organización sin fines de lucro?','¿Te atrae la idea de trabajar en un banco?','¿Te gusta trabajar con maquinaria y herramientas?','¿Te interesa la ingeniería civil?','¿Te gustaría trabajar en la producción de música?','¿Te atrae la idea de trabajar en un despacho de abogados o estudio jurídico,?','¿Te interesa la biología y la vida marina?','¿Te gustaría trabajar en el área de recursos humanos?','¿Te gusta el análisis de datos?','¿Te interesa la psicología y la salud mental?','¿Te atrae la idea de trabajar en una agencia de publicidad?','¿Te gustaría trabajar en la industria alimentaria?','¿Te sientes atraído/a por el mundo del deporte?','¿Te gustaría trabajar en el área de ventas?','¿Te interesa la mecánica y la tecnología?','¿Te atrae la idea de trabajar en una organización internacional?','¿Te gusta trabajar con animales?','¿Te gustaría trabajar en una revista o periódico?','¿Te interesa la arqueología y la historia antigua?']
    numeros = list(range(1, 31))
    if request.method == 'POST':
        form = TestForm(request.POST)
        if not form.is_valid():
            print("FFFF")
            print("Errores en el formulario:")
            print(form.errors)
            return render(request, 'answers.html', {'form': form, 'id_estudiante': id_estudiante, 'questions': questions, 'numeros': numeros, 'nombre': student.nombre})

        else:
            
            test = form.save()
            print(test.nombre)
            print(test.id_estudiante)
            return redirect('result',id_estudiante=id_estudiante)
    else:
        return render(request, 'answers.html', {'form': form,'id_estudiante': id_estudiante,'questions':questions,'numeros':numeros,'nombre':student.nombre})

def result(request,id_estudiante):
    test  = Test.objects.get(id_estudiante=id_estudiante)
    return render(request,'result.html',{'id_estudiante':id_estudiante,'nombre':test.nombre})
