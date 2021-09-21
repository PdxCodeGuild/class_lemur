
from django.forms import ModelForm
from .models import Checkout

class CheckoutForm(ModelForm):
    class Meta:
        model = Checkout
        fields = '__all__'