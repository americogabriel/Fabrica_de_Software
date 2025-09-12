from django.forms import ModelForm
from .models import Cachorro

class CachorroForm(ModelForm):
    class Meta:
        model = Cachorro
        fields = ["nome","raca","instagram","idade"]
        
