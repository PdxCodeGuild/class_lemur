from django.forms import ModelForm
from .models import Groceries

class GroceriesForm(ModelForm):
    class Meta:
        model = Groceries
        fields = '__all__'