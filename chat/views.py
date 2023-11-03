
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import Chat
import openai
from cuentas.models import Student



openai.api_key = "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"

def chat(request, id_estudiante):
    student = Student.objects.get(id_estudiante=id_estudiante)
    chats = Chat.objects.filter(student=student)
    hist_mssg = [] 
    hist_resp = []  
    for chat in chats:
        hist_mssg.append(chat.message)
        hist_resp.append(chat.response)

    
    if request.method == 'POST':
        message = request.POST.get('message')
        
        with open('chat/script.txt', 'r') as script:
            prompt = script.read()
        messages = [{"role": "system", "content": prompt}]
        for msg, resp in zip(hist_mssg, hist_resp):
            messages.append({"role": "user", "content": msg})
            messages.append({"role": "assistant", "content": resp})
        messages.append({"role": "user", "content": message})
        responses_completition = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages,
            temperature = 1
        )
        response = responses_completition["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": response})        
        chat = Chat(student=student,message=message, response=response, created_at=timezone.now())
        chat.save()
         
        return JsonResponse({'message': message, 'response': response})
    
    return render(request, 'chat.html', {'chats': chats,'student':student,'id_estudiante':id_estudiante})

