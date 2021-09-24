from django.db.models.base import Model
from django.forms import ModelForm 

from .models import Chirp

class ChirpForm(ModelForm):
    
    class Meta:
        model = Chirp
        fields = '__all__'