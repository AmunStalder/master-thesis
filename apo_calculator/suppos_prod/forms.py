from django import forms
from .models import SupposProd
from productions.models import Productions, Ingredient
from substances.models import Substance
from django.forms import inlineformset_factory


class SupposProdForm1(forms.ModelForm):
    class Meta:
        model = SupposProd
        fields = (
            'tara_pouring_bowl',
            'calib_value_suppo_mould',
        )
    def __init__(self, *args, **kwargs):
        super(SupposProdForm1, self).__init__(*args, **kwargs)
        # instance = getattr(self, 'instance', None)
        self.fields['tara_pouring_bowl'].label = 'Tara of pouring bowl incl. porcellain pestle [g]'
        self.fields['tara_pouring_bowl'].widget.attrs['placeholder'] = 'Enter mass'
        self.fields['calib_value_suppo_mould'].label = 'Enter calibration value of suppository mould [g]'
        self.fields['calib_value_suppo_mould'].widget.attrs['placeholder'] = 'Enter mass'

class SupposProdForm2(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = [
            'substance',
            'target_amount_for_bulk',
            'actual_amount_for_bulk',
        ]
    def __init__(self, *args, **kwargs):
        super(SupposProdForm2, self).__init__(*args, **kwargs)

        self.fields['substance'].disabled = True
        self.fields['target_amount_for_bulk'].disabled = True
        self.fields['target_amount_for_bulk'].label = "Target amount for bulk [g]"
        self.fields['actual_amount_for_bulk'].widget.attrs['placeholder'] = "Enter weighed amount of substance in [g]"
        self.fields['actual_amount_for_bulk'].label = "Actual amount for bulk [g]"


inline_SupposProdForm2 = inlineformset_factory(
            Productions,
            Ingredient,
            form=SupposProdForm2,
            can_delete=False,
            extra=0,
            fields=(
                'substance',
                'target_amount_for_bulk',
                'actual_amount_for_bulk',
                    ),
            )


class SupposProdForm3(forms.ModelForm):

    class Meta:
        model = SupposProd
        fields = [
            'actual_mass_bulk_incl_tara',
        ]
    def __init__(self, *args, **kwargs):
        super(SupposProdForm3, self).__init__(*args, **kwargs)
        self.fields['actual_mass_bulk_incl_tara'].label = "Mass of bulk incl tara of pouring bowl and Rührer [g]"
        self.fields['actual_mass_bulk_incl_tara'].widget.attrs['placeholder'] = "Enter mass"



# class SupposProdForm3(forms.ModelForm):
#
#     class Meta:
#         model = SupposProd
#         fields = [
#             'production',
#             'active_substance_1',
#             'conc_per_suppo',
#             'amount_of_suppos',
#             'calibration_value',
#         ]
#     def __init__(self, *args, **kwargs):
#         super(SupposProdForm3, self).__init__(*args, **kwargs)
#         self.fields['production'].label = 'Production'
#         self.fields['production'].queryset = Productions.objects.filter(galenical_form='suppositories')
#         self.fields['production'].disabled = True
#         self.fields['active_substance_1'].label = 'Active substance'
#         self.fields['active_substance_1'].widget.attrs['placeholder'] = 'Choose the active substance'
#         # self.fields['active_substance_1'].disabled = True
#         self.fields['conc_per_suppo'].label = 'Concentration per suppository [mg]'
#         self.fields['conc_per_suppo'].widget.attrs['placeholder'] = 'Enter desired concentration of active substance per suppository'
#         self.fields['amount_of_suppos'].label = 'Amount of suppositories (incl. excess) [pc.]'
#         self.fields['amount_of_suppos'].widget.attrs['placeholder'] = 'Enter amount of suppositories to produce inluding about 10-20% excess'
#         self.fields['calibration_value'].label = 'Calibration value of suppository mould [g]'
#         self.fields['calibration_value'].widget.attrs['placeholder'] = 'Enter calibration value'

#
# class SupposProdForm4(forms.ModelForm):
#     class Meta:
#         model = SupposProd
#         fields = [
#             'required_mass_active_substance',
#             'weighed_mass_active_substance',
#             'required_mass_witepsol',
#             'weighed_mass_witepsol',
#         ]
#
#     def __init__(self, *args, **kwargs):
#         super(SupposProdForm4, self).__init__(*args, **kwargs)
#         # instance = getattr(self, 'instance', None)
#         self.fields['required_mass_active_substance'].disabled = True
#         self.fields['required_mass_active_substance'].label = 'Required mass of active substance [mg] (precalculated)'
#         self.fields['weighed_mass_active_substance'].label = 'Weighed mass of active  substance [mg]'
#         self.fields['weighed_mass_active_substance'].widget.attrs['placeholder'] = 'Enter mass'
#         self.fields['required_mass_witepsol'].label = 'Required mass of witepsol [g]'
#         self.fields['required_mass_witepsol'].disabled = True


# class SupposProdForm3(forms.ModelForm):
#     class Meta:
#         model = Ingredient
#         fields = [
#             'production',
#             'substance',
#             'target_amount',
#             'actual_amount',
#             'price_per_amount',
#         ]
    # def __init__(self, *args, **kwargs):
    #     super(SupposProdForm3, self).__init__(*args, **kwargs)
    #     # instance = getattr(self, 'instance', None)
    #     self.fields['production'].label = 'Production'
    #     self.fields['production'].disabled = True
