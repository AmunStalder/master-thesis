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
            'required_amount_of_tabs',
            'amount_of_weighed_tabs',
            'mass_all_tabs',
        ]

    def __init__(self, *args, **kwargs):
        super(CapsProdForm2, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['required_amount_of_tabs'].disabled = True


class CapsProdForm3(forms.ModelForm):
    class Meta:
        model = CapsProd
        fields = [
            'weighed_mass_powder',
            'caps_size',
        ]
        
class CapsProdForm4(forms.ModelForm):
    class Meta:
        model = CapsProd
        fields = [
            'tara_meas_cylinder',
            'required_volume',
            'mass_required_volume',
        ]

    def __init__(self, *args, **kwargs):
        super(CapsProdForm4, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['required_volume'].disabled = True
