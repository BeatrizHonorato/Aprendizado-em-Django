from django.shortcuts import render, redirect, get_object_or_404
from .models import Professor

def criar_professor(request):
    if request.method == 'GET':
        return render(request, 'criar_professor.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        professor = Professor(nome = nome, email = email, senha = senha)
        professor.save()
        return redirect('criar_professor')

def visualizar_professor(request):
    if request.method == 'GET':
       professor = Professor.objects.all()
       return render(request, 'visualizar_professor.html', {'professor' : professor})
    
    
def deletar_professor(request, id):
    professor = get_object_or_404(Professor, id=id)
    professor.delete()
    return redirect('visualizar_professor')
       

