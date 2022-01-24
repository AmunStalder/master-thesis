from django import forms

class CapsulesUniformityOfMass(forms.Form):
    mass_1_caps_empty = forms.FloatField(label='Mass of 1 empty capsules [g]')
    mass_20_caps_full = forms.FloatField(label='Mass of 20 full capsules [g]')
    mass_max1 = forms.FloatField(label='Mass of heaviest capsule [g]')
    mass_min1 = forms.FloatField(label='Mass of lightest capsule [g]')
