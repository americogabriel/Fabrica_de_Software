from django.forms import ModelForm
from .models import Usuarios

class PessoaForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['user','idade','email']