from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RespuestaForm
from .models import Respuesta

def home(request):
    
    return render(request,'home.html')


def test(request):
    return render(request,'test.html')

def answers(request):
    return render(request,'answers.html')

