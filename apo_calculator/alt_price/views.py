from .forms import SupposALTPriceForm
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, FileResponse
from . import models
import math
from django.urls import reverse_lazy

class ALTPriceCreateView(CreateView):
    template_name = 'alt_price/altprice_form.html'
    model = models.ALTPrice

    def get_form_class(self):
        if models.Productions.objects.get(pk=self.kwargs['pk']).galenical_form == "suppositories":
            return SupposALTPriceForm

    def get_initial(self):
        production = models.Productions.objects.get(pk=self.kwargs['pk'])
        if production.dose_units > 12:
            suppos_other_12 = math.ceil(production.dose_units / 12 - 1)
            suppos_box_up_to_12 = suppos_other_12+1
        else:
            suppos_other_12 = 0
            suppos_box_up_to_12 = suppos_other_12+1
        return { 'production': production, 'suppos_other_12': suppos_other_12, 'suppos_box_up_to_12':suppos_box_up_to_12}
