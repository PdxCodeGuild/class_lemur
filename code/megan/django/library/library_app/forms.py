from django.db.models.base import Model
from django.forms import ModelForm 

from .models import Checked

class LibraryForm(ModelForm):
    
    class Meta:
        model = Checked
        fields = '__all__'


