from django import forms
from .models import Productions, Ingredient
from substances.models import Substance

class ProductionsForm(forms.ModelForm):
    class Meta:
        model = Productions
        fields = [
            'galenical_form',
            'lot_nr',
            'name',
        ]

#can be commented out if ingredient is chosen during prod
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'production',
            'substance',
        ]
    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)

        self.fields['production'].disabled = True
        # Filter for ingredients that have a displacement value

        self.fields['substance'].queryset = Substance.objects.filter(displacement_value__isnull = False)
        self.fields['substance'].label = 'Substance'
