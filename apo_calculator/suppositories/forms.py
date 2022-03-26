from django import forms
from .models import SupposUniformity
from productions.models import Productions

class SupposUniformityForm(forms.ModelForm):
    class Meta:
        model = SupposUniformity
        fields = [
            'production',
            'mass_10_suppos',
            'mass_max1',
            'mass_max2',
            'mass_max3',
            'mass_min1',
            'mass_min2',
            'mass_min3',
        ]
    def __init__(self, *args, **kwargs):
        super(SupposUniformityForm, self).__init__(*args, **kwargs)
        # Select only suppositories
        self.fields['production'].queryset = Productions.objects.filter(galenical_form='suppositories')
        # Change labels and placeholders
        self.fields['mass_10_suppos'].label = 'Mass of 10 suppositories [g]'
        self.fields['mass_10_suppos'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_max1'].label = 'Mass of heaviest suppository [g]'
        self.fields['mass_max1'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_max2'].label = 'Mass of second heaviest suppository [g]'
        self.fields['mass_max2'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_max3'].label = 'Mass of third heaviest suppository [g]'
        self.fields['mass_max3'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_min1'].label = 'Mass of lightest suppository [g]'
        self.fields['mass_min1'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_min2'].label = 'Mass of second lightest suppository [g]'
        self.fields['mass_min2'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_min3'].label = 'Mass of third lightest suppository [g]'
        self.fields['mass_min3'].widget.attrs['placeholder'] = 'Enter mass'
