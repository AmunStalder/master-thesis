from django.views.generic import TemplateView
from .forms import UniformityForm
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from . import models

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
        'mass_min1',
    )

class CapsUnifUpdateView(UpdateView):
    fields = (
        'caps_name',
        'mass_1_caps_empty',
        'mass_20_caps_full',
        'mass_max1',
        'mass_min1',
    )
    model = models.Uniformity
    # def form_valid(self, form):
    #     # Threshold to determine if +/- 10 or 15% apply for uniformity
    #     THRESHOLD_CAPS = 0.3
    #     mass_1_caps_empty = form.cleaned_data['mass_1_caps_empty']
    #     mass_20_caps_full = form.cleaned_data['mass_20_caps_full']
    #     mass_max1 = form.cleaned_data['mass_max1']
    #     mass_min1 = form.cleaned_data['mass_min1']
    #     mean_content = mass_20_caps_full/20 - mass_1_caps_empty
    #     if mean_content <= THRESHOLD_CAPS:
    #         diff = 0.1
    #     else:
    #         diff = 0.15
    #     upper1 = mean_content*(1+diff)
    #     upper2 = mean_content*(1+2*diff)
    #     lower1 = mean_content*(1-diff)
    #     lower2 = mean_content*(1-2*diff)
    #     print(form.cleaned_data)
    #     return super().form_valid(form)
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


# class ResultView(TemplateView):
#     template_name = 'capsules/result.html'
