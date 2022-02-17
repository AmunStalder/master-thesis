from django import forms
from .models import Productions

class ProductionsForm(forms.ModelForm):
    class Meta:
        model = Productions
        fields = [
            'galenical_form',
            'lot_nr',
            'name',
        ]
