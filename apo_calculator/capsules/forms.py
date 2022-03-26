from django import forms
from .models import Uniformity
from productions.models import Productions

class UniformityForm(forms.ModelForm):
    class Meta:
        model = Uniformity
        fields = [
            'production',
            'mass_1_caps_empty',
            'mass_20_caps_full',
            'mass_max1',
            'mass_max2',
            'mass_max3',
            'mass_min1',
            'mass_min2',
            'mass_min3',
        ]
    def __init__(self, *args, **kwargs):
        super(UniformityForm, self).__init__(*args, **kwargs)
        # Select only capsules
        self.fields['production'].queryset = Productions.objects.filter(galenical_form='capsules')
        # Change labels and placeholders
        self.fields['mass_1_caps_empty'].label = 'Mass of 1 empty capsule [mg]'
        self.fields['mass_1_caps_empty'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_20_caps_full'].label = 'Mass of 20 filled capsules [mg]'
        self.fields['mass_20_caps_full'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_max1'].label = 'Mass of heaviest capsule [mg]'
        self.fields['mass_max1'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_max2'].label = 'Mass of second heaviest capsule [mg]'
        self.fields['mass_max2'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_max3'].label = 'Mass of third heaviest capsule [mg]'
        self.fields['mass_max3'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_min1'].label = 'Mass of lightest capsule [mg]'
        self.fields['mass_min1'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_min2'].label = 'Mass of second lightest capsule [mg]'
        self.fields['mass_min2'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['mass_min3'].label = 'Mass of third lightest capsule [mg]'
        self.fields['mass_min3'].widget.attrs['placeholder'] = 'Enter mass'
