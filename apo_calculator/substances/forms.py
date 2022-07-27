from django import forms
from .models import FinishedMedicinalProduct

class FinishedMedicinalProductForm(forms.ModelForm):
    class Meta:
        model = FinishedMedicinalProduct
        fields = [
            'name',
            'main_ingredient',
            'manufacturer',
            'galenical_form',
            'dose_units_per_package',
            'conc_per_dose_unit_mg',
            'price_chf',
        ]
    def __init__(self, *args, **kwargs):
        super(FinishedMedicinalProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Name of finished medicinal product'
        self.fields['name'].widget.attrs['placeholder'] = 'Enter name'
        self.fields['manufacturer'].widget.attrs['placeholder'] = 'Enter manufacturer name'
        self.fields['galenical_form'].label = 'Galenical form'
        self.fields['galenical_form'].widget.attrs['placeholder'] = 'Enter form'
        self.fields['main_ingredient'].label = 'Active ingredient'
        self.fields['main_ingredient'].widget.attrs['placeholder'] = 'Enter Activ ingredient'
        self.fields['dose_units_per_package'].label = 'Dose units per package'
        self.fields['dose_units_per_package'].widget.attrs['placeholder'] = 'Enter dose units'
        self.fields['conc_per_dose_unit_mg'].label = 'Dose per dose unit [mg]'
        self.fields['conc_per_dose_unit_mg'].widget.attrs['placeholder'] = 'Enter dose per dose unit in mg!'
        self.fields['price_chf'].label = 'Price of one package [CHF]'
        self.fields['price_chf'].widget.attrs['placeholder'] = 'Enter price'
