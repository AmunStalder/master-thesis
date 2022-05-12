from django.views.generic import DetailView, DeleteView
from formtools.wizard.views import SessionWizardView
from django.forms.models import construct_instance
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
import math

from productions.models import Productions, Ingredient
from .models import SupposProd
from .forms import SupposProdForm1, SupposProdForm2
from substances.models import Substance

class SupposProdWizardView(SessionWizardView):
    template_name = "suppos_prod/prod_form.html"
    form_list = [SupposProdForm1, SupposProdForm2]
    instance = None

    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})
        #we define initial values for steps
        if step == '1':
            data = self.get_cleaned_data_for_step('0')
            required_mass_active_substance = data['amount_of_suppos']*data['conc_per_suppo']
            #M = N *(E -f*A), where M = required mass witepsol
            N = data['amount_of_suppos']
            E = data['calibration_value']
            #this was changed
            f = Substance.objects.get(name=data['active_substance_1']).displacement_value
            A = data['conc_per_suppo']/1000
            required_mass_witepsol = N*(E - f*A)
            initial.update({'required_mass_active_substance': round(required_mass_active_substance,4)})
            initial.update({'required_mass_witepsol': round(required_mass_witepsol,4)})
        return initial

    def get_form_instance(self, step):
        #if instance already exists (for update)
        try:
            self.instance = SupposProd.objects.get(pk=self.kwargs['pk'])
        #for new calculation make new instance and prefill with production
        #that was given by kwargs (pk=production.pk)
        except:
            self.instance = SupposProd()
            self.instance.production = Productions.objects.get(pk=self.kwargs['pk'])
            self.instance.active_substance_1 = Ingredient.objects.get(production=Productions.objects.get(pk=self.kwargs['pk']))
        return self.instance

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        #in step 2 some calculations are performed on the input data of step 0
        #and passed ad context data to step 1.
        # if self.steps.current == '1':
        #     data = self.get_cleaned_data_for_step('0')
        #     context.update(data)
        # if self.steps.current == '2':
        #     data1 = self.get_cleaned_data_for_step('0')
        #     data2 = self.get_cleaned_data_for_step('1')
        #     needed_amount_of_tabs = data1['amount_of_caps']*data1['conc_per_cap'] / data1['conc_per_tab']
        #     required_mass_powder = round( needed_amount_of_tabs * data2['mass_all_tabs'] / data2['amount_of_weighed_tabs'],4)
        #     data2['required_mass_powder'] = required_mass_powder
        #     context.update(data1)
        #     context.update(data2)
        #
        # if self.steps.current == '3':
        #     data = self.get_all_cleaned_data()
        #     required_volume = data['caps_size']*data['amount_of_caps']
        #     data['required_volume'] = required_volume
        #     context.update(data)

        return context

    def done(self, form_list, **kwargs):
        for form in form_list:
            self.instance = construct_instance(form, self.instance, form._meta.fields, form._meta.exclude)
        self.instance.save()
        return redirect("suppos_prod:detail", pk=self.instance.pk)

class SupposProdDetailView(DetailView):
    model = Productions
    template_name = 'suppos_prod/detail.html'

class SupposProdDeleteView(DeleteView):
    model = SupposProd
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy("productions:detail", kwargs={'pk':pk})
