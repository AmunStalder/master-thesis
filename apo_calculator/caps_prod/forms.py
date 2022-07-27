from django import forms
from .models import CapsProd
from productions.models import Productions, Ingredient


class CapsProdForm1(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'required_amount_of_tabs',
            'required_amount_of_tabs_incl_excess',
            'weight_tabs_incl_excess',
        ]

    def __init__(self, *args, **kwargs):
        super(CapsProdForm1, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['required_amount_of_tabs'].disabled = True
        self.fields['required_amount_of_tabs'].label = 'Required amount of tablets [pc.] (precalculated)'
        self.fields['required_amount_of_tabs_incl_excess'].label = 'Amount of tablets used for mortaring (about 10% excess)[pc.]'
        self.fields['weight_tabs_incl_excess'].label = 'Total mass of tablets for mortaring [mg]'
        self.fields['weight_tabs_incl_excess'].widget.attrs['placeholder'] = 'Enter the total mass of tablets used for mortaring'


class CapsProdForm2(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'target_amount_for_bulk',
            'actual_amount_for_bulk',
        ]
    def __init__(self, *args, **kwargs):
        super(CapsProdForm2, self).__init__(*args, **kwargs)
        self.fields['target_amount_for_bulk'].label = 'Mass of required tablet powder [mg]'
        self.fields['target_amount_for_bulk'].disabled = True
        self.fields['actual_amount_for_bulk'].label = 'Weighed tablet powder [mg]'

class CapsProdForm3(forms.ModelForm):
    class Meta:
        model = CapsProd
        fields = [
            'caps_size',
        ]
    def __init__(self, *args, **kwargs):
        super(CapsProdForm3, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['caps_size'].label = 'Capsule size'

class CapsProdForm4(forms.ModelForm):
    class Meta:
        model = CapsProd
        fields = [
            'required_volume',
            'tara_meas_cylinder',
            'mass_required_volume_incl_tara',
        ]
    def __init__(self, *args, **kwargs):
        super(CapsProdForm4, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['required_volume'].label = 'Required volume for measuring cylinder [ml]'
        self.fields['required_volume'].disabled = True
        self.fields['tara_meas_cylinder'].label = 'Tara of measuring cylinder pre-coated with Mannitol [g]'
        self.fields['tara_meas_cylinder'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_required_volume_incl_tara'].label = 'Mass of measuring cylinder inkl requireed volume of powder [g]'
        self.fields['mass_required_volume_incl_tara'].widget.attrs['placeholder'] = 'Enter mass'

class CapsProdForm5(forms.ModelForm):
    class Meta:
        model = CapsProd
        fields = [
            'mass_required_volume',
        ]
    def __init__(self, *args, **kwargs):
        super(CapsProdForm5, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['mass_required_volume'].label = 'The mass of the powdermix is:'
        self.fields['mass_required_volume'].disabled = True
