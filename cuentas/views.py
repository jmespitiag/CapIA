from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm, StudentRegister
from django.contrib.auth import authenticate, login


def home(request,id_estudiante):
    
    return render(request,'home.html',{'id_estudiante': id_estudiante})

def home_name(request):
    if request.method == 'POST':
        form = StudentForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home', id_estudiante=user.id_estudiante) 
    else:
        form = StudentForm()

    return render(request, 'home_name.html', {'form': form})

def register(request):
    print(request.method)
    if request.method == 'POST':
        form = StudentRegister(request.POST)
        if form.is_valid(): 
            print('yes')
            registed = form.save()
            if registed.universitario:
                return redirect('home',id_estudiante=registed.id_estudiante)
            else:
                return redirect('test',id_estudiante=registed.id_estudiante)
        else:
            print(form.errors)
            return render(request, 'register_errors.html', {'form': form})
    else:
        initial_data = {'carrera': 'N/A'}
        form = StudentRegister(initial_data)
    return render(request,'register.html',{'form':form})
        
        