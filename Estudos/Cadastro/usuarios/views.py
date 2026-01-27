from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cadastrar_usuario(request):
    return render(request, 'usuarios/cadastrar_usuarios.html')

def login(request):
    return render(request, 'usuarios/login.html')
