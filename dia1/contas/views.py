from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
from .models import Transaçao
from .form import TransacaoForm


def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    data['nomes'] = ['vitoria','gabriel','artur','tati']
    #html =f"<html><body><h1>O horario atual é de: {now}</h1></body></html>" 
    return render(request,'contas/home.html',data)

def listagem(request):
    data = {}
    data['transaçoes'] = Transaçao.objects.all()
    
    return render(request,'contas/listagem.html',data)

def nova_transacao(request):
    if request.method == 'POST':
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_inicio')
    else:
        form = TransacaoForm()
    data = {}
    data['form'] = form
    return render(request,'contas/form.html',data)

def update(request,pk):
    update = Transaçao.objects.get(id=pk)
    form = TransacaoForm(request.POST or None,instance=update)
    if form.is_valid():
        form.save()
        return redirect('url_inicio')
        
    data = {}
    data['form'] = form
    data['object'] = update
    return render(request,'contas/form.html',data)

def delete(request,pk):
    form = Transaçao.objects.get(id=pk)
    try:
        form.delete()
        return redirect('url_inicio')
    except Exception as erro:
        return HttpResponse(f"Não foi possível acessar seu formulário: {erro}")
    

    


       