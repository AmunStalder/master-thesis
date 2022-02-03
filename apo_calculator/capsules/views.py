from django.views.generic import TemplateView
from .forms import UniformityForm
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy

# Create your views here.

#View for Capsules
class CapsFuncView(TemplateView):
    template_name = 'capsules/functions.html'
# Create your views here.

class CapsUnifListView(ListView):
    context_object_name = 'caps_list'
    model = models.Uniformity
    template_name = 'capsules/list.html'

class CapsUnifDetailView(DetailView):
    context_object_name = 'caps_detail'
    model = models.Uniformity
    template_name = 'capsules/detail.html'

class CapsUnifCreateView(CreateView):
    template_name = 'capsules/uniformity_form.html'
    model = models.Uniformity
    fields = (
        'caps_name',
        'mass_1_caps_empty',
        'mass_20_caps_full',
        'mass_max1',
        'mass_max2',
        'mass_max3',
        'mass_min1',
        'mass_min2',
        'mass_min3',
    )

class CapsUnifUpdateView(UpdateView):
    fields = (
        'caps_name',
        'mass_1_caps_empty',
        'mass_20_caps_full',
        'mass_max1',
        'mass_max2',
        'mass_max3',
        'mass_min1',
        'mass_min2',
        'mass_min3',
    )
    model = models.Uniformity

class CapsUnifDeleteView(DeleteView):
    context_object_name = 'uniformity'
    model = models.Uniformity
    success_url = reverse_lazy("capsules:list")
