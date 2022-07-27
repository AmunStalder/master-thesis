from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, FileResponse
from . import models
from .forms import FinishedMedicinalProductForm
from django.urls import reverse_lazy
# from .utils import render_to_pdf
#Import the easy_pdf rendering

# Create your views here.

class SubstanceListView(ListView):
    context_object_name = "substances_list"
    model = models.Substance
    template_name = 'substances/list.html'

class SubstanceDetailView(DetailView):
    model = models.Substance
    template_name = 'substances/detail.html'

class FinishedMedicinalProductListView(ListView):
    context_object_name = 'finishedmedicinalproducts_list'
    model = models.FinishedMedicinalProduct
    template_name = 'substances/fmp-list.html'

class FinishedMedicinalProductDetailView(DetailView):
    model = models.FinishedMedicinalProduct
    template_name = 'substances/fmp-detail.html'

class FinishedMedicinalProductCreateView(CreateView):
    template_name = 'substances/finishedmedicinalproduct_form.html'
    model = models.FinishedMedicinalProduct
    form_class = FinishedMedicinalProductForm

class FinishedMedicinalProductUpdateView(UpdateView):
    model = models.FinishedMedicinalProduct
    form_class = FinishedMedicinalProductForm

class FinishedMedicinalProductDeleteView(DeleteView):
    model = models.FinishedMedicinalProduct
    success_url = reverse_lazy("substances:fmp-list")
