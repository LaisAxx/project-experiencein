# experiencein/perfis/views.py 
from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all()})

def exibir(request, perfil_id):

    # perfil = Perfil()

    # if perfil_id == 1:
    #     perfil = Perfil('Fábio Henrique', 'fabio.oliveira@ifb.edu.br', '222222', 'IFB')
    
    # if perfil_id == 2:
    #     perfil = Perfil('Elon Musk', 'elon.musk@tesla.com', '333333', 'Tesla') 

    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfil.html', {'perfil':perfil})

