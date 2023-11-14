from django.shortcuts import render, redirect
from .models import Student
from PruebaVocacional.models import Test
from PruebaVocacional.models import Test
from .forms import StudentForm, StudentRegister, StudentChange
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
                if user.universitario:
                    login(request, user)
                    return redirect('home', id_estudiante=user.id_estudiante) 
                else:
                    instance = Test.objects.filter(id_estudiante=user.id_estudiante).exists()
                    if instance:
                        return redirect('home', id_estudiante=user.id_estudiante) 
                    else:
                        return redirect('test', id_estudiante=user.id_estudiante) 
                        
        else:
            print(form.errors)
            return render(request, 'home_name_errors.html', {'form': form})
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

def profile(request,id_estudiante):
    user = Student.objects.get(id_estudiante=id_estudiante)
    if user.universitario:
        return render(request,'profile.html',{'user':user})
    else:
        if request.method == 'POST':
            test = Test.objects.get(id_estudiante=user)
            form = StudentChange(request.POST,instance=test)
            if form.is_valid():
                test.area = form.cleaned_data['area']
                test.save()
                user.universitario = True
                user.save()
                return render(request,'profile.html',{'user':user, 'test': test})
            else:
                print(form.errors)
        
        else:
            test = Test.objects.get(id_estudiante=user)
            form = StudentChange(instance=test)
        return render(request,'profile.html',{'user':user, 'form':form, 'test': test})
            