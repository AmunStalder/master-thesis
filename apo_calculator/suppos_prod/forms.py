from django import forms
from .models import SupposProd
from productions.models import Productions

class SupposProdForm1(forms.ModelForm):
    class Meta:
        model = SupposProd
        fields = [
            'production',
            'active_substance_1',
            'conc_per_suppo',
            'amount_of_suppos',
            'calibration_value',
        ]
    def __init__(self, *args, **kwargs):
        super(SupposProdForm1, self).__init__(*args, **kwargs)
        self.fields['production'].label = 'Production'
        self.fields['production'].queryset = Productions.objects.filter(galenical_form='suppositories')
        self.fields['production'].disabled = True
        self.fields['active_substance_1'].label = 'Active substance'
        self.fields['active_substance_1'].widget.attrs['placeholder'] = 'Choose the active substance'
        self.fields['conc_per_suppo'].label = 'Concentration per suppository [mg]'
        self.fields['conc_per_suppo'].widget.attrs['placeholder'] = 'Enter desired concentration of active substance per suppository'
        self.fields['amount_of_suppos'].label = 'Amount of suppositories (incl. excess) [pc.]'
        self.fields['amount_of_suppos'].widget.attrs['placeholder'] = 'Enter amount of suppositories to produce inluding about 10-20% excess'
        self.fields['calibration_value'].label = 'Calibration value of suppository mould [g]'
        self.fields['calibration_value'].widget.attrs['placeholder'] = 'Enter calibration value'

class SupposProdForm2(forms.ModelForm):
    class Meta:
        model = SupposProd
        fields = [
            'required_mass_active_substance',
            'weighed_mass_active_substance',
            'required_mass_witepsol',
            'weighed_mass_witepsol',
        ]

    def __init__(self, *args, **kwargs):
        super(SupposProdForm2, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        self.fields['required_mass_active_substance'].disabled = True
        self.fields['required_mass_active_substance'].label = 'Required mass of active substance [mg] (precalculated)'
        self.fields['weighed_mass_active_substance'].label = 'Weighed mass of active  substance [mg]'
        self.fields['weighed_mass_active_substance'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['required_mass_witepsol'].label = 'Required mass of witepsol [g]'
        self.fields['required_mass_witepsol'].disabled = True


# class SupposProdForm3(forms.ModelForm):
#     class Meta:
#         model = SupposProd
#         fields = [
#             'weighed_mass_powder',
#             'Suppos_size',
#         ]
#     def __init__(self, *args, **kwargs):
#         super(SupposProdForm3, self).__init__(*args, **kwargs)
#         self.fields['weighed_mass_powder'].label = 'Mass of required tablet powder [mg] *'
#         self.fields['weighed_mass_powder'].widget.attrs['placeholder'] = 'Enter the amount of weighed tablet powder'
#         self.fields['Suppos_size'].label = 'Choose an appopriate Supposule size'
#
# class SupposProdForm4(forms.ModelForm):
#     class Meta:
#         model = SupposProd
#         fields = [
#             'required_volume',
#             'tara_meas_cylinder',
#             'mass_required_volume',
#         ]
#     def __init__(self, *args, **kwargs):
#         super(SupposProdForm4, self).__init__(*args, **kwargs)
#         instance = getattr(self, 'instance', None)
#         self.fields['required_volume'].disabled = True
        # self.fields['required_volume'].label = 'Required volume of powdermix [mg] *'
        # self.fields['tara_meas_cylinder'].widget.attrs['placeholder'] = 'Enter mass (tara) of coated measuring cylinder'
        # self.fields['tara_meas_cylinder'].label = 'Tara of measuring cylinder'
        # self.fields['mass_required_volume'].widget.attrs['placeholder'] = 'Enter mass of weighed powdermix'
        # self.fields['mass_required_volume'].label = 'Tara of measuring cylinder'
