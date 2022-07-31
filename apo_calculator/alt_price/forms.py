from django import forms
from .models import ALTPrice

class SupposALTPriceForm(forms.ModelForm):
    class Meta:
        model = ALTPrice
        fields = [
            'production',
            'suppos_up_to_12',
            'suppos_other_12',
            'suppos_box_up_to_12',
        ]
    def __init__(self, *args, **kwargs):
        super(SupposALTPriceForm, self).__init__(*args, **kwargs)
        self.fields['production'].disabled = True
        self.fields['suppos_up_to_12'].disabled = True
        self.fields['suppos_up_to_12'].label = 'Preparation of suppo mass and production of suppos, up to 12 pcs.'
        self.fields['suppos_other_12'].label = 'Preparation of suppo mass and production of suppos, every further 12 pcs.'
        self.fields['suppos_other_12'].widget.attrs['placeholder'] = 'Add amount'
        self.fields['suppos_box_up_to_12'].label = 'Amount of suppository boxes for packaging (1 box for up to 12 pcs.)'
        self.fields['suppos_box_up_to_12'].widget.attrs['placeholder'] = 'Add amount'

class CapsALTPriceForm(forms.ModelForm):
    class Meta:
        model = ALTPrice
        fields = [
            'production',
            'caps_mixing',
            'caps_sieving',
            'caps_up_to_25',
            'caps_other_25',
            'caps_shell_25',
            'pulvis_50_ml',
            'pulvis_100_ml',
        ]
    def __init__(self, *args, **kwargs):
        super(CapsALTPriceForm, self).__init__(*args, **kwargs)
        self.fields['production'].disabled = True
        self.fields['caps_mixing'].disabled = True
        self.fields['caps_mixing'].label = 'Mixing of powders'
        self.fields['caps_sieving'].label = 'Sieving of powders'
        self.fields['caps_up_to_25'].label = 'Filling of capsules, up to 25 pcs.'
        self.fields['caps_other_25'].label = 'Filling of capsules, every other 25 pcs.'
        self.fields['caps_shell_25'].label = 'Amount of capsule shells, per 25 pcs'
        self.fields['pulvis_50_ml'].label = 'Amount of 50 ml pulvis used for packaging'
        self.fields['pulvis_100_ml'].label = 'Amount of 100 ml pulvis used for packaging'
