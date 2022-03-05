from formtools.wizard.views import SessionWizardView
from .models import CapsProd
from django.forms.models import construct_instance
from django.shortcuts import redirect
import math

class CapsProdWizardView(SessionWizardView):
    template_name = "caps_prod/prod_form.html"

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        if self.steps.current == '1':
            data = self.get_all_cleaned_data()
            total_amount = data['amount_of_caps']*data['conc_per_cap']
            needed_amount_of_tabs = round(total_amount / data['conc_per_tab'],2)
            suggested_amount_of_tabs = math.ceil(needed_amount_of_tabs * 1.1)
            data['total_amount'] = total_amount
            data['needed_amount_of_tabs'] = needed_amount_of_tabs
            data['suggested_amount_of_tabs'] = suggested_amount_of_tabs
            context.update(data)
        if self.steps.current == '2':
            data = self.get_all_cleaned_data()
            needed_amount_of_tabs = data['amount_of_caps']*data['conc_per_cap'] / data['conc_per_tab']
            required_mass_powder = needed_amount_of_tabs * data['mass_all_tabs'] / data['amount_of_weighed_tabs']
            data['required_mass_powder'] = required_mass_powder
            context.update(data)
        return context

    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})
        if step == '1':
            data = self.get_cleaned_data_for_step('0')
            required_amount_of_tabs = data['amount_of_caps']*data['conc_per_cap'] / data['conc_per_tab']
            initial.update({'required_amount_of_tabs': required_amount_of_tabs})
        return initial

    def done(self, form_list, **kwargs):
        new = CapsProd()
        for form in form_list:
            new = construct_instance(form, new, form._meta.fields, form._meta.exclude)
        new.save()
        return redirect('/')
    #
    # def get_template_names(self):
    #     """
    #     Custom templates for the different steps
    #     """
    #     return [TEMPLATES[self.steps.current]]
