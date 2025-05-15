from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def cursos(request):
    return render(request, 'cursos.html')
def contatos(request):
    return render(request, 'contatos.html')