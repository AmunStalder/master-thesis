from django.views.generic import DetailView, DeleteView
from formtools.wizard.views import SessionWizardView
from django.forms.models import construct_instance
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .forms import CapsProdForm1, CapsProdForm2, CapsProdForm3, CapsProdForm4, CapsProdForm5
import math

from productions.models import Productions, Ingredient
from .models import CapsProd

class CapsProdWizardView(SessionWizardView):
    template_name = "caps_prod/prod_form.html"
    form_list = [CapsProdForm1, CapsProdForm2, CapsProdForm3, CapsProdForm4, CapsProdForm5]
    instance1 = None
    instance2 = None

    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})
        # production = Productions.objects.get(pk = self.kwargs['pk'])
        # ingredient = production.ingredient_set.get(is_filler_excipient = False)
        # excipient = production.ingredient_set.get(is_filler_excipient = True)
        if step == '0':
            pass
        if step == '1':
            data = self.get_cleaned_data_for_step('0')
            target_amount_for_bulk = round(self.instance1.required_amount_of_tabs * data['weight_tabs_incl_excess'] / self.instance1.required_amount_of_tabs_incl_excess,1)
            initial.update({"target_amount_for_bulk": target_amount_for_bulk})
        if step == '3':
            data = self.get_cleaned_data_for_step('2')
            required_volume = data['caps_size']*self.instance2.production.dose_units_incl_excess
            initial.update({"required_volume": required_volume})
        if step == '4':
            data = self.get_cleaned_data_for_step('3')
            data1 = self.get_cleaned_data_for_step('1')
            mass_required_volume = data['mass_required_volume_incl_tara']-data['tara_meas_cylinder']
            mannitol = Ingredient.objects.get(production = Productions.objects.get(pk = self.kwargs['pk']), is_filler_excipient = True)
            mannitol.actual_amount_for_bulk = mass_required_volume/1000-data1['actual_amount_for_bulk']
            mannitol.save()

            initial.update({"mass_required_volume": mass_required_volume})
        # ingredient.save()
        return initial

    def get_form_instance(self, step):
        #if instance already exists (for update)
        if step == '0' or step == '1':
            # self.instance = Productions.objects.get(pk=self.kwargs['pk'])
            self.instance1 = Ingredient.objects.get(production=Productions.objects.get(pk = self.kwargs['pk']), is_filler_excipient = False )
            #for new calculation make new instance and prefill with production
            #that was given by kwargs (pk=production.pk)
            # self.SupposProdInstance.active_substance_1 = Ingredient.objects.get(production=Productions.objects.get(pk=self.kwargs['pk']))
            return self.instance1
        else:
            try:
                self.instance2 = CapsProd.objects.get(production=Productions.objects.get(pk = self.kwargs['pk']))
            except:
                self.instance2 = CapsProd()
                self.instance2.production = Productions.objects.get(pk=self.kwargs['pk'])
            return self.instance2

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        return context

    def done(self, form_list, **kwargs):
        for form in form_list[0:2]:
            for i in [0,1]:
                instance = construct_instance(form, self.instance1, form._meta.fields, form._meta.exclude)
                print(self.instance1)

        self.instance1.save()
        for form in form_list[2:5]:
            self.instance = construct_instance(form, self.instance2, form._meta.fields, form._meta.exclude)
            print(self.instance)
        self.instance2.save()
        return redirect("productions:detail", pk=self.instance1.production.pk)

    # def done(self, form_list, **kwargs):
    #     #Save ingredients
    #     if form_list[1].is_valid():
    #         form_list[1].save()
    #     for form in [form_list[0]]:
    #         self.instance = construct_instance(form, self.instance, form._meta.fields, form._meta.exclude)
    #     self.instance.save()



class CapsProdDetailView(DetailView):
    model = Productions
    template_name = 'caps_prod/detail.html'

class CapsProdDeleteView(DeleteView):
    model = CapsProd
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy("productions:detail", kwargs={'pk':pk})
