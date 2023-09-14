
from django.shortcuts import render, redirect
from django.http import HttpResponse

def chat(request,id_estudiante):
    return render(request,'chat.html',{'id_estudiante':id_estudiante})
