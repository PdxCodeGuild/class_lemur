from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm

class CreateForm(UserCreationForm):
    class Meta:
        fields = '__all__'