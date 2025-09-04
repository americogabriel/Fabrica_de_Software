from django.forms import ModelForm
from .models import Transaçao


class TransacaoForm(ModelForm):
    class Meta:
        model = Transaçao
        fields = ['data','descrição','valor','categoria','observaçao']

