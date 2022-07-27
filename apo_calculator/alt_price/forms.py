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
