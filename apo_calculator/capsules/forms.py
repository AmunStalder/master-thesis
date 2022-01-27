from django import forms
from .models import Uniformity

class UniformityForm(forms.ModelForm):
    class Meta:
        model = Uniformity
        fields = [
            'caps_name',
            'mass_1_caps_empty',
            'mass_20_caps_full',
            'mass_max1',
            'mass_min1',
        ]
