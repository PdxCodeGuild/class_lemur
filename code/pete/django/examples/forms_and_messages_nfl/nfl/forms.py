from django.forms import ModelForm, TextInput

from .models import Player

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        # fields = ('first_name', 'last_name', 'team',) # list individal fields
        fields = '__all__'
        widgets = {
            'first_name': TextInput(attrs={
                'style': 'background-color: red;',
            }),
        }