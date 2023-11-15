from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Test
from cuentas.models import Student
from .forms import TestForm




        
        
        


def test(request,id_estudiante):
    return render(request,'test.html',{'id_estudiante': id_estudiante})

def answers(request,id_estudiante):
    
    student = Student.objects.get(id_estudiante=id_estudiante)
    print(student.nombre)
    print(student.id_estudiante)
    questions =['¿Te gusta trabajar con números y fórmulas?','¿Te gustaría trabajar en un laboratorio?','¿Te sientes atraído/a por el mundo de los negocios?','¿Te gusta leer y analizar obras literarias?','¿Te gustaría trabajar en un hospital?','¿Te atrae la idea de diseñar edificios y construcciones?','¿Te gusta crear contenido para redes sociales?','¿Te atrae la idea de investigar nuevos medicamentos?','¿Te interesa la programación de computadoras?','¿Te gustaría trabajar en laindustria cinematográfica?','¿Te sientes atraído/a por el arte y la creatividad?','¿Te gustaría trabajar en una organización sin fines de lucro?','¿Te atrae la idea de trabajar en un banco?','¿Te gusta trabajar con maquinaria y herramientas?','¿Te interesa la ingeniería civil?','¿Te gustaría trabajar en la producción de música?','¿Te atrae la idea de trabajar en un despacho de abogados o estudio jurídico,?','¿Te interesa la biología y la vida marina?','¿Te gustaría trabajar en el área de recursos humanos?','¿Te gusta el análisis de datos?','¿Te interesa la psicología y la salud mental?','¿Te atrae la idea de trabajar en una agencia de publicidad?','¿Te gustaría trabajar en la industria alimentaria?','¿Te sientes atraído/a por el mundo del deporte?','¿Te gustaría trabajar en el área de ventas?','¿Te interesa la mecánica y la tecnología?','¿Te atrae la idea de trabajar en una organización internacional?','¿Te gusta trabajar con animales?','¿Te gustaría trabajar en una revista o periódico?','¿Te interesa la arqueología y la historia antigua?']
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.id_estudiante = student
            form.nombre = student.nombre
            form.area_test = 'N/A'
            form.area = 'N/A'
            form.save()
            return redirect('result', id_estudiante=id_estudiante)
        else:
            print("Errores en el formulario:")
            print(form.errors)
    else:
        form = TestForm(initial={'nombre': student.nombre, 'id_estudiante': id_estudiante})

    return render(request, 'answers.html', {'form': form, 'id_estudiante': id_estudiante, 'questions': questions, 'nombre': student.nombre})

def result(request,id_estudiante):
    test  = Test.objects.get(id_estudiante=id_estudiante)
    areas={1:'Administrativas y contables',2: 'Humanísticas, Ciencias Jurídicas y Sociales',3:'Artísticas',4:'Ciencias de la salud',5:'Ingenierías, carreras técnicas y computación',6:'Ciencias exactas'}
    puntos={1:0,2:0,3:0,4:0,5:0,6:0}
    table = [
    [[1, 6], 5, 4, 2],
    [6, 4, 2, [1, 3]],
    [[1, 2], 5, [4, 6], 3],
    [2, 3, [4, 5], [1, 6]],
    [4, 2, [1, 5, 6], 3],
    [5, 3, [1, 4, 6], 2],
    [3, [1, 2], 4, [5, 6]],
    [4, 5, [1, 2, 6], 3],
    [5, 6, [1, 4], [3, 2]],
    [[2, 3], 5, [1, 6], 4],
    [[2, 3], 5, [4, 6], 1],
    [2, [1, 3], 4, [5, 6]],
    [1, 5, [2, 6], [3, 4]],
    [5, [4, 6], [1, 2], 3],
    [5, 6, 3, 1],
    [3, 2, 5, 4],
    [2, 1, 5, 3],
    [4, 6, 5, 1],
    [2, 1, 1, 3],
    [[1, 6], 5, 2, 3],
    [2, 4, 6, 5],
    [3, 2, 1, 4],
    [4, 2, 1, 3],
    [4, 2, 3, 5],
    [1, 2, 3, 4],
    [5, 6, 4, 2],
    [5, 1, 5, 2],
    [4, 4, 4, 3],
    [2, 3, 1, 4],
    [2, 3, 6, 1]
]
    total_puntos = 0
    for i in range(1,31):
        respuesta = getattr(test,f"respuesta{i}",None)
        if respuesta is not None:
            value = table[i-1][respuesta]
            try:
                for j in value:
                    total_puntos+=1
                    puntos[j] = puntos[j]+1
            except:
                total_puntos+=1
                puntos[value] = puntos[value]+1


    puntos = {k: v for k, v in sorted(puntos.items(), key=lambda item: item[1],reverse=True)}
    print(total_puntos)
    ranking = []
    for clave in puntos:
        area = areas[clave]
        percentage = (puntos[clave]/total_puntos)*100
        percentage = format(percentage, '.2f')
        ranking.append((area,percentage))    
    test.area_test = ranking[0][0]
    test.save()
    print(ranking[0][0])
        
    return render(request,'result.html',{'id_estudiante':id_estudiante,'nombre':test.nombre,'ranking':ranking})

def data(request, id_estudiante):
    student = Student.objects.get(id_estudiante=id_estudiante)
    try:
        test_student = Test.objects.get(id_estudiante=student)
        
        area_student = test_student.area_test
        dates = Test.objects.filter(area_test=area_student)
        coincidencia=0
        fallo=0
        for t in dates:
            print()
            if t.area_test == t.area:
                coincidencia=coincidencia+1
            else:
                fallo=fallo+1
        total = coincidencia + fallo
        porcentaje_coincidencia = (coincidencia/total)*100
        porcentaje_fallo = (fallo/total)*100
        print(total, coincidencia, fallo)

        areas = ['Administrativas y contables', 'Humanísticas, Ciencias Jurídicas y Sociales', 'Artísticas', 'Ciencias de la salud', 'Ingenierías, carreras técnicas y computación', 'Ciencias exactas']

        results={}
        for area in areas:
            results[area] = len(Test.objects.filter(area_test=area_student, area=area))

        return render(request, 'analisis.html', {'id_estudiante': id_estudiante, 'coincidencia': porcentaje_coincidencia, 'fallo': porcentaje_fallo, 'area': area_student, 'admin': results['Administrativas y contables'], 'sociales': results['Humanísticas, Ciencias Jurídicas y Sociales'], 'artes': results['Artísticas'], 'salud': results['Ciencias de la salud'], 'ing': results['Ingenierías, carreras técnicas y computación'], 'exactas': results['Ciencias exactas']})
    except Test.DoesNotExist:
        area_student = "nivel general"
        dates = Test.objects.filter()
        coincidencia=0
        fallo=0
        for t in dates:
            print()
            if t.area_test == t.area:
                coincidencia=coincidencia+1
            else:
                fallo=fallo+1
        total = coincidencia + fallo
        porcentaje_coincidencia = (coincidencia/total)*100
        porcentaje_fallo = (fallo/total)*100
        areas = ['Administrativas y contables', 'Humanísticas, Ciencias Jurídicas y Sociales', 'Artísticas', 'Ciencias de la salud', 'Ingenierías, carreras técnicas y computación', 'Ciencias exactas']

        results={}
        for area in areas:
            results[area] = len(Test.objects.filter(area_test=area))
        
        return render(request, 'analisis.html', {'id_estudiante': id_estudiante, 'coincidencia': porcentaje_coincidencia, 'fallo': porcentaje_fallo, 'area': area_student, 'admin': results['Administrativas y contables'], 'sociales': results['Humanísticas, Ciencias Jurídicas y Sociales'], 'artes': results['Artísticas'], 'salud': results['Ciencias de la salud'], 'ing': results['Ingenierías, carreras técnicas y computación'], 'exactas': results['Ciencias exactas']})
