
from django.shortcuts import render, redirect
from django.http import HttpResponse

def chat(request):
    return render(request,'chat.html')# Create your views here.
