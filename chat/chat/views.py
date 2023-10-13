
from django.shortcuts import render, redirect
from django.http import HttpResponse
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain import PromptTemplate
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from django.http import JsonResponse
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from ctransformers import AutoModelForCausalLM
from django.utils import timezone
from .models import Chat
import torch
import openai
import transformers
from PruebaVocacional.models import Student

DB_FAISS_PATH = 'chat/vectorstore/db_faiss'

custom_prompt_template = """You are a helpful assistant that helps students with their problems based in the context below:

Context: {context}
Question: {question}

Give a correct and straight answer, if you don't know the answer just say I don't know the answer.
Return the answer and nothing else
Helpful answer:
"""

def set_custom_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(template=custom_prompt_template,
                            input_variables=['context', 'question'])
    return prompt

#Retrieval QA Chain
def retrieval_qa_chain(llm, prompt, db):
    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type='stuff',
                                       retriever=db.as_retriever(search_kwargs={'k': 2}),
                                       return_source_documents=True,
                                       chain_type_kwargs={'prompt': prompt}
                                       )
    return qa_chain

#Loading the model
def load_llm():
    # Load the locally downloaded model here
    llm = CTransformers(
        model = "llama-2-7b-chat.ggmlv3.q3_K_L.bin",
        model_type="llama",
        max_new_tokens = 512,
        temperature = 0.5
    )
    return llm

#QA Model Function
def qa_bot():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    qa = retrieval_qa_chain(llm, qa_prompt, db)

    return qa

#output function
def final_result(query):
    qa_result = qa_bot()
    response = qa_result({'query': query})
    return response

openai.api_key = "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"

def chat(request, id_estudiante):
    student = Student.objects.get(id_estudiante=id_estudiante)
    chats = Chat.objects.filter(student=student)
    

    if request.method == 'POST':
        message = request.POST.get('message')
        # response = final_result(message)
        messages = [{"role": "system", "content": "Eres un asistente que ayuda a los estudiantes con problemas emocionales en español"}]
        messages.append({"role": "user", "content": message})
        responses_completition = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages
        )
        response = responses_completition["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": response})

        print(response)

        # Verificar si el usuario está autenticado
        
        chat = Chat(student=student,message=message, response=response, created_at=timezone.now())
        chat.save()
         
        return JsonResponse({'message': message, 'response': response})
    
    return render(request, 'chat.html', {'chats': chats,'student':student})