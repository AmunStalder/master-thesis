from django import forms
from .models import Productions, Ingredient

class ProductionsForm(forms.ModelForm):
    class Meta:
        model = Productions
        fields = [
            'galenical_form',
            'lot_nr',
            'name',
        ]

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
            'production',
            'substance',
        ]
    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        # Select only capsules
        self.fields['production'].queryset = Productions.objects.filter(galenical_form='capsules')
        self.fields['production'].disabled = True
        # Change labels and placeholders
        self.fields['substance'].label = 'Substance'
