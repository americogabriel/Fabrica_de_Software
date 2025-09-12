from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Usuarios, Endereco
from .form import PessoaForm
import requests

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
    

def deletar_pessoa(request, pk):
    pessoa = Usuarios.objects.get(pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('listar_pessoas')
    return render(request, 'confirmar_delete.html', {'pessoa': pessoa})

def atualizar_pessoa(request, pk):
    pessoa = Usuarios.objects.get(pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'create.html', {'pessoa': form})


def consultarcep(request):
    response = requests.get('https://viacep.com.br/ws/01001000/json/', verify = False)
    dados = response.json()
    Obj = Endereco.objects.create(
        endereco = dados['logradouro'],
        other = dados['ibge'] ,
        email = dados['bairro']
    )
    return HttpResponse(dados['ibge'])