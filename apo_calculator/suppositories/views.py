from django.views.generic import TemplateView
from apo_calculator.utils import render_to_pdf
from . import models
from .forms import SupposUniformityForm
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponse, FileResponse
from . import models
from django.urls import reverse_lazy
from apo_calculator.utils import render_to_pdf
# Create your views here.

#View for Suppositories
class SuppositoriesFunctionsView(TemplateView):
    template_name = 'suppositories/functions.html'
# Create your views here.
class SupposUnifCreateView(CreateView):
    context_object_name = 'suppos_uniformity'
    template_name = 'suppositories/supposuniformity_form.html'
    model = models.SupposUniformity
    form_class = SupposUniformityForm

class SupposUnifPdfView(DetailView):
    context_object_name = 'suppos_uniformity'
    model = models.SupposUniformity
    template_name = 'suppositories/pdf.html'

    def get_context_data(self, **kwargs):
        context = super(SupposUnifPdfView, self).get_context_data(**kwargs)
        # add extra context if needed
        return context

class SupposUnifDetailView(DetailView):
    context_object_name = 'suppos_uniformity'
    model = models.SupposUniformity
    template_name = 'suppositories/detail.html'

class SupposUnifUpdateView(UpdateView):
    model = models.SupposUniformity
    form_class = SupposUniformityForm

class SupposUnifDeleteView(DeleteView):
    context_object_name = 'suppos_uniformity'
    model = models.SupposUniformity

    success_url = reverse_lazy("productions:list" )
