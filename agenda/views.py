from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ola_mundo(request):
    return HttpResponse('<p>Olá! Está é minha primeira view com DJANGO!</p>')

def pagina_inicial(request):
    return render(request, 'agenda/index.html')