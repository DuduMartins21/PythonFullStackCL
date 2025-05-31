# app01/views.py
from django.shortcuts import render, redirect
from .forms import ContatoForm
from .models import Curso, Contato # <--- AGORA IMPORTE TAMBÉM O MODELO Contato

def cursos(request):
    todos_cursos = Curso.objects.all()
    context = {
        'cursos': todos_cursos
    }
    return render(request, 'app01/cursos.html', context)

def home(request):
    return render(request, 'app01/home.html')

def teste_template(request):
    return render(request, 'app01/base.html')

def contatos(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            # NOVO: Crie e salve uma nova entrada no modelo Contato
            Contato.objects.create(
                nome=nome,
                email=email,
                mensagem=mensagem
            )

            print(f"Dados Recebidos E SALVOS - Nome: {nome}, Email: {email}, Mensagem: {mensagem}")

            # Certifique-se de que aqui esteja apenas 'contatos' (sem 'app01:')
            return redirect('contatos')
    else:
        form = ContatoForm()

    return render(request, 'app01/contatos.html', {'form': form})

