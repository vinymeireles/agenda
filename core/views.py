from django.shortcuts import redirect, render, redirect
from core.models import Evento

# Create your views here.
""" def query(request, titulo_evento):
    consulta = Evento.object.get(titulo='titulo_evento')
    return consulta """

""" #redirecionar a pagina sempre para agenda = index
def index(request): 
    return redirect('/agenda') """

def lista_eventos(request):
   usuario = request.user 
  # evento = Evento.objects.filter(usuario=usuario) acessa com o login do usuario
   evento = Evento.objects.all()
   dados = {'eventos': evento}
   return render(request, 'agenda.html', dados)    #redirecionar para a pagina agenda.html