from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Usuarios
from .form import PessoaForm


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


def criarpessoas(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_listarpessoas')
    else:
        data = {}
        data['pessoa'] = PessoaForm()
        return render(request,'app/criar.html', data)