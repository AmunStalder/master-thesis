from django.views.generic import ListView, DetailView
from django.http import HttpResponse, FileResponse
from . import models
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
#
#class ProductionCreateView(CreateView):
#     template_name = 'productions/productions_form.html'
#     model = models.Productions
#     fields = (
#         'galenical_form',
#         'lot_nr',
#         'name',
#     )
#
# class ProductionUpdateView(UpdateView):
#     model = models.Productions
#     fields = (
#         'galenical_form',
#         'lot_nr',
#         'name',
#     )
#
# class ProductionDeleteView(DeleteView):
#     model = models.Productions
#     success_url = reverse_lazy("productions:list")
