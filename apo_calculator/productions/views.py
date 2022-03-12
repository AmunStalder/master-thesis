from .forms import ProductionsForm
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, FileResponse
from . import models
from django.urls import reverse_lazy
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
    context_object_name = 'production'
    model = models.Productions
    template_name = 'productions/detail.html'

# class CapsUnifPdfView(DetailView):
#     context_object_name = 'caps_detail'
#     model = models.Uniformity
#     template_name = 'capsules/pdf.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(CapsUnifPdfView, self).get_context_data(**kwargs)
#         # add extra context if needed
#         return context
#
#     def render_to_response(self, context, **kwargs):
#         pdf = render_to_pdf(self.template_name, context)
#         return HttpResponse(pdf, content_type='application/pdf')
#


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
    context_object_name = 'production'
    model = models.Productions
    success_url = reverse_lazy("productions:list")
