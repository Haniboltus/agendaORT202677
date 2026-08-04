from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contato
from .forms import ContatoForm

# Create your views here.
def ola_mundo(request):
    return HttpResponse('<p>Olá! Está é minha primeira view com DJANGO!</p>')

def pagina_inicial(request):
    return render(request, 'agenda/index.html')

#Retorna todos os contatos da agenda
def contato_lista(request):
    #ORM (Object-Relational Mapping)
    contatos = Contato.objects.all()
    #Renderiza o html passando a lista de contatos
    return render(request, 'agenda/contatos_lista.html', {'contatos' : contatos})

def contato_criar(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda:contato_lista')
    else:
        form = ContatoForm()

    return render(request, 'agenda/contato_form.html', {'form' : form})
