from .forms import ProductionsForm, SupposIngredientForm, CapsIngredientForm, SupposFillerForm, CapsFillerForm, AMBVValueForm
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


class ProductionPdfView(DetailView):
    model = models.Productions
    template_name = 'productions/pdf.html'

    def get_context_data(self, **kwargs):
        context = super(ProductionPdfView, self).get_context_data(**kwargs)
        is_pdf = True
        # add extra context if needed
        context['is_pdf'] = is_pdf
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')


class ProductionCreateView(CreateView):
    template_name = 'productions/productions_form.html'
    model = models.Productions
    form_class = ProductionsForm

class ProductionUpdateView(UpdateView):
    model = models.Productions
    form_class = ProductionsForm

class ProductionDeleteView(DeleteView):
    model = models.Productions
    success_url = reverse_lazy("productions:list")

class IngredientCreateView(CreateView):
    template_name = 'productions/Ingredient_form.html'
    model = models.Ingredient
    #choose ingredient form with pre-selection of possible substances based on galenical form
    def get_form_class(self):
        if models.Productions.objects.get(pk=self.kwargs['pk']).galenical_form == "suppositories":
            if models.Productions.objects.get(pk=self.kwargs['pk']).ingredient_set.exists():
                return SupposIngredientForm
            else:
                return SupposFillerForm

        elif models.Productions.objects.get(pk=self.kwargs['pk']).galenical_form == "capsules":
            if models.Productions.objects.get(pk=self.kwargs['pk']).ingredient_set.exists():
                return CapsIngredientForm
            else:
                return CapsFillerForm

    def get_initial(self):
        return { 'production': models.Productions.objects.get(pk=self.kwargs['pk']) }

class IngredientUpdateView(UpdateView):
    model = models.Ingredient
    def get_form_class(self):
        if models.Ingredient.objects.get(pk=self.kwargs['pk']).production.galenical_form == "suppositories":
            if not models.Ingredient.objects.get(pk=self.kwargs['pk']).is_filler_excipient:
                return SupposIngredientForm
            else:
                return SupposFillerForm
        elif models.Ingredient.objects.get(pk=self.kwargs['pk']).production.galenical_form == "capsules":
            if not models.Ingredient.objects.get(pk=self.kwargs['pk']).is_filler_excipient:
                return CapsIngredientForm
            else:
                return CapsFillerForm

    def get_initial(self):
        return { 'production': models.Ingredient.objects.get(pk=self.kwargs['pk']).production }

class IngredientDeleteView(DeleteView):
    model = models.Ingredient
    def get_success_url(self):
        ingredient = models.Ingredient.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy("productions:detail", kwargs={'pk':ingredient.production.pk})

class AMBVValueCreateView(CreateView):
    template_name = 'productions/ambvvalue_form.html'
    model = models.AMBVValue
    form_class = AMBVValueForm
    def get_initial(self):
        return { 'production': models.Productions.objects.get(pk=self.kwargs['pk']) }

class AMBVValueUpdateView(UpdateView):
    model = models.AMBVValue
    form_class = AMBVValueForm
