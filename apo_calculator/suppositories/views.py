from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from apo_calculator.utils import render_to_pdf
from django.http import HttpResponse, FileResponse
from django.urls import reverse_lazy
from . import models
from .forms import SupposUniformityForm
from productions.models import Productions
# Create your views here.


class SupposUnifCreateView(CreateView):
    template_name = 'suppositories/supposuniformity_form.html'
    model = Productions
    form_class = SupposUniformityForm
    def get_initial(self):
        return { 'production': Productions.objects.get(pk=self.kwargs['pk']) }

class SupposUnifDetailView(DetailView):
    model = Productions
    template_name = 'suppositories/detail.html'
#View for Suppositories
# class SuppositoriesFunctionsView(TemplateView):
#     template_name = 'suppositories/functions.html'
# Create your views here.
class SupposUnifUpdateView(UpdateView):
    model = models.SupposUniformity
    form_class = SupposUniformityForm

# class SupposUnifPdfView(DetailView):
#     context_object_name = 'suppos_uniformity'
#     model = Productions
#     template_name = 'suppositories/pdf.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(SupposUnifPdfView, self).get_context_data(**kwargs)
#         # add extra context if needed
#         return context

class SupposUnifDeleteView(DeleteView):
    model = models.SupposUniformity
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy("productions:detail", kwargs={'pk':pk})
