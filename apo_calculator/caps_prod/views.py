from formtools.wizard.views import SessionWizardView
from .models import CapsProd
from django.views.generic import DetailView, DeleteView
from django.forms.models import construct_instance
from django.shortcuts import redirect
from productions.models import Productions
from django.urls import reverse, reverse_lazy
import math

class CapsProdWizardView(SessionWizardView):
    template_name = "caps_prod/prod_form.html"
    instance = None


    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})

        #we define initial values for steps
        if step == '1':
            data = self.get_cleaned_data_for_step('0')
            required_amount_of_tabs = round(data['amount_of_caps']*data['conc_per_cap'] / data['conc_per_tab'],4)
            initial.update({'required_amount_of_tabs': required_amount_of_tabs})
        if step == '3':
            data = self.get_cleaned_data_for_step('0')
            data1 = self.get_cleaned_data_for_step('2')
            required_volume = data['amount_of_caps']*data1['caps_size']
            initial.update({'required_volume': required_volume})
        return initial

    def get_form_instance(self, step):
        #if instance already exists (for update)
        try:
            self.instance = CapsProd.objects.get(pk=self.kwargs['pk'])
        #for new calculation make new instance and prefill with production
        #that was given by kwargs (pk=production.pk)
        except:
            self.instance = CapsProd()
            self.instance.production = Productions.objects.get(pk=self.kwargs['pk'])
        return self.instance

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        #in step 2 some calculations are performed on the input data of step 0
        #and passed ad context data to step 1.
        if self.steps.current == '1':
            data = self.get_cleaned_data_for_step('0')
            total_amount = data['amount_of_caps']*data['conc_per_cap']
            needed_amount_of_tabs = round(total_amount / data['conc_per_tab'],4)
            suggested_amount_of_tabs = math.ceil(needed_amount_of_tabs * 1.1)
            data['total_amount'] = total_amount
            data['needed_amount_of_tabs'] = needed_amount_of_tabs
            data['suggested_amount_of_tabs'] = suggested_amount_of_tabs
            context.update(data)
        if self.steps.current == '2':
            data1 = self.get_cleaned_data_for_step('0')
            data2 = self.get_cleaned_data_for_step('1')
            needed_amount_of_tabs = data1['amount_of_caps']*data1['conc_per_cap'] / data1['conc_per_tab']
            required_mass_powder = round( needed_amount_of_tabs * data2['mass_all_tabs'] / data2['amount_of_weighed_tabs'],4)
            data2['required_mass_powder'] = required_mass_powder
            context.update(data1)
            context.update(data2)

        if self.steps.current == '3':
            data = self.get_all_cleaned_data()
            required_volume = data['caps_size']*data['amount_of_caps']
            data['required_volume'] = required_volume
            context.update(data)

        return context

    def done(self, form_list, **kwargs):
        for form in form_list:
            self.instance = construct_instance(form, self.instance, form._meta.fields, form._meta.exclude)
        self.instance.save()
        return redirect("productions:detail", pk=self.instance.pk)

class CapsProdDetailView(DetailView):
    model = CapsProd
    template_name = 'caps_prod/detail.html'

class CapsProdDeleteView(DeleteView):
    model = CapsProd
    def get_success_url(self):
        pk = self.kwargs['pk']
        print(pk)
        return reverse_lazy("productions:detail", kwargs={'pk':pk})
    #
    # def get_template_names(self):
    #     """
    #     Custom templates for the different steps
    #     """
    #     return [TEMPLATES[self.steps.current]]
