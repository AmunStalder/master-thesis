from .forms import ProductionsForm, IngredientForm
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, FileResponse
from . import models
from django.urls import reverse_lazy
from .utils import render_to_pdf

# from .utils import render_to_pdf
#Import the easy_pdf rendering

# Create your views here.

#View for Capsules
class ProductionFuncView(TemplateView):
    template_name = 'productions/functions.html'
# Create your views here.

class ProductionListView(ListView):
    context_object_name = 'productions_list'
    model = models.Productions
    template_name = 'productions/list.html'

class ProductionDetailView(DetailView):
    model = models.Productions
    template_name = 'productions/detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ProductionDetailView, self).get_context_data(**kwargs)
    #     pk = self.kwargs['pk']
    #     obj = self.model.objects.get(pk=pk)
    #     if hasattr(obj, 'uniformity') and hasattr(obj, 'capsprod'):
    #
    #         calculated_mass_powder_mix = obj.uniformity.mean*obj.capsprod.amount_of_caps
    #         absolute_mass_balance = calculated_mass_powder_mix - obj.capsprod.mass_required_volume
    #         relative_mass_balance = absolute_mass_balance / obj.capsprod.mass_required_volume
    #         mass_balance_release_note = ""
    #         if relative_mass_balance <= 0.1 and relative_mass_balance >= -0.1:
    #             mass_balance_release_note = True
    #         else:
    #             mass_balance_release_note = False
    #         context["calculated_mass_powder_mix"] = calculated_mass_powder_mix
    #         context["absolute_mass_balance"] = absolute_mass_balance
    #         context["relative_mass_balance"] = relative_mass_balance
    #         context["mass_balance_release_note"] = mass_balance_release_note
    #     return context

class ProductionPdfView(DetailView):
    model = models.Productions
    template_name = 'productions/pdf.html'

    def get_context_data(self, **kwargs):
        context = super(ProductionPdfView, self).get_context_data(**kwargs)
        # add extra context if needed
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')


class ProductionCreateView(CreateView):
    template_name = 'productions/productions_form.html'
    model = models.Productions
    fields = (
        'galenical_form',
        'lot_nr',
        'name',
    )

class ProductionUpdateView(UpdateView):
    model = models.Productions
    fields = (
        'galenical_form',
        'lot_nr',
        'name',
    )
class ProductionDeleteView(DeleteView):
    model = models.Productions
    success_url = reverse_lazy("productions:list")

class IngredientCreateView(CreateView):
    template_name = 'productions/Ingredient_form.html'
    model = models.Ingredient
    form_class = IngredientForm
    def get_initial(self):
        return { 'production': models.Productions.objects.get(pk=self.kwargs['pk']) }

class IngredientUpdateView(UpdateView):
    model = models.Ingredient
    form_class = IngredientForm

class IngredientDeleteView(DeleteView):
    model = models.Ingredient
    success_url = reverse_lazy("productions:list")
