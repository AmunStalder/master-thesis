from django import forms
from .models import CapsProd

class CapsProdForm1(forms.ModelForm):
    class Meta:
        model = CapsProd
        fields = [
            'production',
            'amount_of_caps',
            'conc_per_cap',
            'conc_per_tab',
        ]

class CapsProdForm2(forms.ModelForm):
    class Meta:
        model = CapsProd
        fields = [
            'amount_of_weighed_tabs',
            'mass_all_tabs',
            'required_mass_powder',
            'weighed_mass_powder',
            'caps_size',
        ]
