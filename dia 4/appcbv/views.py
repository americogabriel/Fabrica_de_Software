from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from .models import Cachorro
from .forms import CachorroForm
from django.urls import reverse_lazy


# Create your views here.
class HelloView(View):
    frase = 'Boa tarde meu patrão'
    def get(self, request):
        return HttpResponse(self.frase)

class CachorroListView(ListView):
    model = Cachorro
    template_name = "list_dog.html"
    context_object_name = "cachorros"

class CreateCachorro(CreateView):
    model = Cachorro
    form_class = CachorroForm
    template_name = 'createcachorro.html'
    success_url = reverse_lazy('listar_cachorros')

class CachorroUpdate(UpdateView):
    model = Cachorro
    form_class = CachorroForm
    template_name = 'createcachorro.html'
    context_object_name = 'cachorroupdate'
    success_url = reverse_lazy('listar_cachorros')

class CachorroDelete(DeleteView):
    model = Cachorro
    template_name = 'delete.html'
    context_object_name = 'cachorro'
    success_url = reverse_lazy('lista_cachorros')




