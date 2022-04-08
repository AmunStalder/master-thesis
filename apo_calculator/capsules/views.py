from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from apo_calculator.utils import render_to_pdf
from django.http import HttpResponse, FileResponse
from django.urls import reverse_lazy

from . import models
from .forms import UniformityForm
from productions.models import Productions
#Import the easy_pdf rendering

# Create your views here.

#View for Capsules
# class CapsFuncView(TemplateView):
#     template_name = 'capsules/functions.html'
# # Create your views here.
#
# class CapsUnifListView(ListView):
#     context_object_name = 'caps_list'
#     model = models.Uniformity
#     template_name = 'capsules/list.html'
class CapsUnifCreateView(CreateView):
    template_name = 'capsules/uniformity_form.html'
    model = Productions
    form_class = UniformityForm
    def get_initial(self):
        return { 'production': Productions.objects.get(pk=self.kwargs['pk']) }

class CapsUnifDetailView(DetailView):
    model = Productions
    template_name = 'capsules/detail.html'

# class CapsUnifPdfView(DetailView):
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

class CapsUnifUpdateView(UpdateView):
    model = models.Uniformity
    form_class = UniformityForm

class CapsUnifDeleteView(DeleteView):
    model = models.Uniformity
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy("productions:detail", kwargs={'pk':pk})
