from .forms import UniformityForm
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponse, FileResponse
from . import models
from django.urls import reverse_lazy
from apo_calculator.utils import render_to_pdf
from .forms import UniformityForm
from productions.models import Productions
#Import the easy_pdf rendering

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

class CapsUnifPdfView(DetailView):
    context_object_name = 'caps_detail'
    model = models.Uniformity
    template_name = 'capsules/pdf.html'

    def get_context_data(self, **kwargs):
        context = super(CapsUnifPdfView, self).get_context_data(**kwargs)
        # add extra context if needed
        return context

    def render_to_response(self, context, **kwargs):
        pdf = render_to_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type='application/pdf')

class CapsUnifCreateView(CreateView):
    template_name = 'capsules/uniformity_form.html'
    model = models.Uniformity
    form_class = UniformityForm
    def get_initial(self):
        return { 'production': Productions.objects.get(pk=self.kwargs['pk']) }


class CapsUnifUpdateView(UpdateView):
    model = models.Uniformity
    form_class = UniformityForm

class CapsUnifDeleteView(DeleteView):
    context_object_name = 'uniformity'
    model = models.Uniformity

    success_url = reverse_lazy("productions:list" )
