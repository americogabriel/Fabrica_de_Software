from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuarios

def home(request):
    return render(request,'app/home.html')


def hello(request):
    return HttpResponse("<h1>Hello User")

def listarpessoas(request):
    usuario = request.user
    data = {}
    data['pessoas'] = Usuarios.objects.all()
    data['logado'] = usuario.username
    return render (request,'app/list.html',data)

