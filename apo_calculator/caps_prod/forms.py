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
    def __init__(self, *args, **kwargs):
        super(CapsProdForm1, self).__init__(*args, **kwargs)
        self.fields['production'].label = 'Production'
        self.fields['amount_of_caps'].label = 'Amount of capsules [pc.]'
        self.fields['amount_of_caps'].widget.attrs['placeholder'] = 'Enter amount of capsules to produce'
        self.fields['conc_per_cap'].label = 'Concentration per capsule [mg]'
        self.fields['conc_per_cap'].widget.attrs['placeholder'] = 'Enter the final concentration of active ingredient per capsule'
        self.fields['conc_per_tab'].label = 'Concentration per tablet [mg]'
        self.fields['conc_per_tab'].widget.attrs['placeholder'] = 'Enter the concentration of active ingredient per tablet that are used for mortar'

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
        self.fields['required_amount_of_tabs'].label = 'Required amount of tablets [pc.] (precalculated)'
        self.fields['amount_of_weighed_tabs'].label = '*Amount of tablets used for mortaring [pc.]'
        self.fields['amount_of_weighed_tabs'].widget.attrs['placeholder'] = 'Enter the actual amount of tablets that you use for mortaring (about 10% excess from required amount)'
        self.fields['mass_all_tabs'].label = 'Total mass of tablets for mortaring [mg]'
        self.fields['mass_all_tabs'].widget.attrs['placeholder'] = 'Enter the total mass of tablets used for mortaring'


class CapsProdForm3(forms.ModelForm):
    class Meta:
        model = CapsProd
        fields = [
            'weighed_mass_powder',
            'caps_size',
        ]
    def __init__(self, *args, **kwargs):
        super(CapsProdForm3, self).__init__(*args, **kwargs)
        self.fields['weighed_mass_powder'].label = 'Mass of required tablet powder [mg] *'
        self.fields['weighed_mass_powder'].widget.attrs['placeholder'] = 'Enter the amount of weighed tablet powder'
        self.fields['caps_size'].label = 'Choose an appopriate capsule size'

class CapsProdForm4(forms.ModelForm):
    class Meta:
        model = CapsProd
        fields = [
            'required_volume',
            'tara_meas_cylinder',
            'mass_required_volume',
        ]
    def __init__(self, *args, **kwargs):
        super(CapsProdForm4, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['required_volume'].disabled = True
        # self.fields['required_volume'].label = 'Required volume of powdermix [mg] *'
        # self.fields['tara_meas_cylinder'].widget.attrs['placeholder'] = 'Enter mass (tara) of coated measuring cylinder'
        # self.fields['tara_meas_cylinder'].label = 'Tara of measuring cylinder'
        # self.fields['mass_required_volume'].widget.attrs['placeholder'] = 'Enter mass of weighed powdermix'
        # self.fields['mass_required_volume'].label = 'Tara of measuring cylinder'
