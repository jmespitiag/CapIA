from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Test
import pandas as pd
from .forms import TestForm

def home(request):
    return render(request,'home.html')


def test(request):
    return render(request,'test.html')

def answers(request):
    data = {}  # Diccionario para almacenar las respuestas por pregunta

    if request.method == 'POST':
        for i in range(1, num_preguntas + 1):  # Ajusta num_preguntas al número de preguntas que tienes
            form = TestForm(request.POST)
            respuesta = request.POST.get(f'respuesta_{i}')

            if form.is_valid():
                pregunta = f'Pregunta_{i}'  # Nombre de la pregunta
                data[pregunta] = [respuesta]  # Almacenar la respuesta en el diccionario

                test_instance = form.save(commit=False)
                test_instance.respuesta = respuesta
                # Resto de tu código para procesar y guardar la instancia de Test
                # ...
                test_instance.save()
    
        # Crear un DataFrame con los datos recolectados
        df = pd.DataFrame(data)

        # Guardar el DataFrame en un archivo CSV
        df.to_csv('respuestas.csv', index=False)

        # Redirige o muestra una página de confirmación después de procesar todas las respuestas
        return redirect('confirmacion')
    else:
        form = TestForm()

    return render(request, 'answers.html', {'form': form})
