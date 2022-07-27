from django.views.generic import DetailView, DeleteView
from formtools.wizard.views import SessionWizardView
from django.forms.models import construct_instance

from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
import math

from productions.models import Productions, Ingredient
from .models import SupposProd
from .forms import SupposProdForm1, inline_SupposProdForm2, SupposProdForm3
from substances.models import Substance

class SupposProdWizardView(SessionWizardView):
    template_name = "suppos_prod/prod_form.html"
    form_list = [SupposProdForm1, inline_SupposProdForm2, SupposProdForm3]
    instance = None

    def get_form_initial(self, step):
        initial = self.initial_dict.get(step, {})
        #we define initial values for steps
        if step == '1':
            data = self.get_cleaned_data_for_step('0')
            #M = N *(E -f*A), where M = required mass witepsol
            production = Productions.objects.get(pk = self.kwargs['pk'])
            N = production.dose_units_incl_excess
            E = data['calib_value_suppo_mould']
            #this was changed
            sum = 0
            for ingredient in Ingredient.objects.filter(production=Productions.objects.get(pk = self.kwargs['pk'])).exclude(substance = Substance.objects.get(name="Witepsol H-15 Pastillenform/en pastilles")):
                sum = sum + ingredient.substance.displacement_value * ingredient.conc_per_dose_unit / 1000
            witepsol = Ingredient.objects.get(production=production, substance=Substance.objects.get(name="Witepsol H-15 Pastillenform/en pastilles"))
            witepsol.target_amount_for_bulk = round(N*(E - sum),4)
            witepsol.save()
        return initial

    def get_form_instance(self, step):
        #if instance already exists (for update)
        if step != '1':
            # self.instance = Productions.objects.get(pk=self.kwargs['pk'])
            try:
                self.instance = SupposProd.objects.get(production=Productions.objects.get(pk = self.kwargs['pk']))
            #for new calculation make new instance and prefill with production
            #that was given by kwargs (pk=production.pk)
            except:
                self.instance = SupposProd()
                self.instance.production = Productions.objects.get(pk=self.kwargs['pk'])
                # self.SupposProdInstance.active_substance_1 = Ingredient.objects.get(production=Productions.objects.get(pk=self.kwargs['pk']))
        else:
            self.instance = Productions.objects.get(pk = self.kwargs['pk'])
        return self.instance



    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)
        prod = Productions.objects.get(pk = self.kwargs['pk'])
        ingredient_count = prod.ingredient_set.count
        context["ingredient_count"] = ingredient_count
        return context

    def done(self, form_list, **kwargs):
        #Save ingredients
        if form_list[1].is_valid():
            form_list[1].save()
        for form in [form_list[0]]:
            self.instance = construct_instance(form, self.instance, form._meta.fields, form._meta.exclude)
        self.instance.save()

        return redirect("productions:detail", pk=self.kwargs['pk'])

class SupposProdDetailView(DetailView):
    model = Productions
    template_name = 'suppos_prod/detail.html'

class SupposProdDeleteView(DeleteView):
    model = SupposProd
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy("productions:detail", kwargs={'pk':pk})
