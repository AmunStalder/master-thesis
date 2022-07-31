from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from apo_calculator.utils import render_to_pdf
from django.http import HttpResponse, FileResponse
from django.urls import reverse_lazy

from . import models
from .forms import UniformityForm
from productions.models import Productions

class CapsUnifCreateView(CreateView):
    template_name = 'capsules/uniformity_form.html'
    model = Productions
    form_class = UniformityForm
    def get_initial(self):
        return { 'production': Productions.objects.get(pk=self.kwargs['pk']) }

class CapsUnifDetailView(DetailView):
    model = Productions
    template_name = 'capsules/detail.html'

class CapsUnifUpdateView(UpdateView):
    model = models.Uniformity
    form_class = UniformityForm

class CapsUnifDeleteView(DeleteView):
    model = models.Uniformity
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy("productions:detail", kwargs={'pk':pk})

class CapsInfoView(TemplateView):
    template_name = 'capsules/info.html'
