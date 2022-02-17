from django import forms
from .models import Uniformity

class UniformityForm(forms.ModelForm):
    class Meta:
        model = Uniformity
        fields = [
            'production',
            'mass_1_caps_empty',
            'mass_20_caps_full',
            'mass_max1',
            'mass_max2',
            'mass_max3',
            'mass_min1',
            'mass_min2',
            'mass_min3',
        ]
