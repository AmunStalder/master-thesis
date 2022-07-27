from django import forms
from .models import Productions, Ingredient, AMBVValue
from substances.models import Substance, FinishedMedicinalProduct

class ProductionsForm(forms.ModelForm):
    class Meta:
        model = Productions
        fields = [
            'galenical_form',
            'lot_nr',
            'name',
            'dose_units',
            'dose_units_incl_excess',
        ]
    def __init__(self, *args, **kwargs):
        super(ProductionsForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Name of production'
        self.fields['name'].widget.attrs['placeholder'] = 'E.g. Paracetamol 500mg suppositories 20 pcs.'
        self.fields['dose_units'].label = 'Dose units'
        self.fields['dose_units'].widget.attrs['placeholder'] = 'Enter final amount of dose units excl. excess'
        self.fields['dose_units_incl_excess'].label = 'Dose units incl. excess'
        self.fields['dose_units_incl_excess'].widget.attrs['placeholder'] = 'Enter final amount of dose units incl. excess'


class SupposIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'production',
            'substance',
            'conc_per_dose_unit',
            'is_filler_excipient',
        ]
    def __init__(self, *args, **kwargs):
        super(SupposIngredientForm, self).__init__(*args, **kwargs)

        self.fields['production'].disabled = True
        # Filter for ingredients that have a displacement value and an ALT Price
        self.fields['substance'].queryset = Substance.objects.filter(displacement_value__isnull = False).exclude(infos = "nALT")
        self.fields['substance'].label = 'Substance'
        self.fields['conc_per_dose_unit'].label = 'Concentration per suppository [mg]'
        self.fields['is_filler_excipient'].label = 'Is it a filling agent?'
        self.initial['is_filler_excipient'] = False
        self.fields['is_filler_excipient'].disabled = True


class SupposFillerForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'production',
            'substance',
            'is_filler_excipient',
        ]
    def __init__(self, *args, **kwargs):
        super(SupposFillerForm, self).__init__(*args, **kwargs)
        self.fields['production'].disabled = True
        self.initial['substance'] = Substance.objects.get(name = 'Witepsol H-15 Pastillenform/en pastilles')
        self.fields['substance'].label = 'Filling agent'
        self.fields['substance'].disabled = True
        self.fields['is_filler_excipient'].label = 'Is it a filling agent?'
        self.initial['is_filler_excipient'] = True
        self.fields['is_filler_excipient'].disabled = True

class CapsFillerForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'production',
            'substance',
            'is_filler_excipient',
        ]
    def __init__(self, *args, **kwargs):
        super(CapsFillerForm, self).__init__(*args, **kwargs)
        self.fields['production'].disabled = True
        self.initial['substance'] = Substance.objects.get(name = 'D(+)-Mannitolum Ph. Eur')
        self.fields['substance'].label = 'Filling agent'
        self.fields['substance'].disabled = True
        self.fields['is_filler_excipient'].label = 'Is it a filling agent?'
        self.initial['is_filler_excipient'] = True
        self.fields['is_filler_excipient'].disabled = True


class CapsIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'production',
            'fmp',
            'conc_per_dose_unit',
        ]
    def __init__(self, *args, **kwargs):
        super(CapsIngredientForm, self).__init__(*args, **kwargs)

        self.fields['production'].disabled = True
        self.fields['fmp'].label = 'Tablets to use'
        self.fields['conc_per_dose_unit'].label = 'Concentration of active pharmaceutical ingredient per capsule [mg]'
        self.fields['conc_per_dose_unit'].widget.attrs['placeholder'] = 'Enter mass'

class AMBVValueForm(forms.ModelForm):
    class Meta:
        model = AMBVValue
        fields = [
            'production',
            'roa',
            'yearly_amount',
            'inherent_risk',
            'manuf_process',
            'contract_manuf',
        ]
    def __init__(self, *args, **kwargs):
        super(AMBVValueForm, self).__init__(*args, **kwargs)

        self.fields['production'].disabled = True
        self.fields['roa'].label = 'Route of application (ROA)'
        self.fields['roa'].widget.attrs['placeholder'] = 'Choose ROA'
        self.fields['yearly_amount'].label = 'Yearly amount of single dosages'
        self.fields['yearly_amount'].widget.attrs['placeholder'] = 'Choose amount by ROA'
        self.fields['inherent_risk'].label = 'Inherent risk of substances'
        self.fields['inherent_risk'].widget.attrs['placeholder'] = 'Choose risk'
        self.fields['manuf_process'].label = 'Type of manufacturing process'
        self.fields['manuf_process'].widget.attrs['placeholder'] = 'Choose type'
        self.fields['contract_manuf'].label = 'Contract manufacturing vs. own customers'
        self.fields['contract_manuf'].widget.attrs['placeholder'] = 'Choose ratio'
        # Filter for ingredients that have a displacement value
