from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class CreateForm(UserCreationForm):
    class Meta:
        fields = '__all__'