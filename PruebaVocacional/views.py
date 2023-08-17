from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RespuestaForm
from .models import Respuesta

def home(request):
    return render(request,'home.html')


def test(request):
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  
        else:
            print(form.errors)
    else:
        form = RespuestaForm()

    context = {'form': form}
    return render(request, 'test.html', context)