from .forms import SupposALTPriceForm, CapsALTPriceForm
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
        elif models.Productions.objects.get(pk=self.kwargs['pk']).galenical_form == "capsules":
            return CapsALTPriceForm
        else:
            pass
    def get_initial(self):
        if models.Productions.objects.get(pk=self.kwargs['pk']).galenical_form == "suppositories":
            production = models.Productions.objects.get(pk=self.kwargs['pk'])
            suppos_up_to_12 = 1
            if production.dose_units > 12:
                suppos_other_12 = math.ceil(production.dose_units / 12 - 1)
                suppos_box_up_to_12 = suppos_other_12+1
            else:
                suppos_other_12 = 0
                suppos_box_up_to_12 = suppos_other_12+1
            return { 'production': production, 'suppos_other_12': suppos_other_12, 'suppos_box_up_to_12':suppos_box_up_to_12, 'suppos_up_to_12':suppos_up_to_12,}
        elif models.Productions.objects.get(pk=self.kwargs['pk']).galenical_form == "capsules":
            production = models.Productions.objects.get(pk=self.kwargs['pk'])
            if production.dose_units > 25:
                caps_other_25 = math.ceil(production.dose_units / 25 - 1)
                caps_shell_25 = caps_other_25+1
            else:
                caps_other_25 = 0
                caps_shell_25 = caps_other_25+1
            caps_mixing = 1
            caps_sieving = 1
            caps_up_to_25 = 1
            return {
                'production': production,
                'caps_mixing':caps_mixing,
                'caps_sieving': caps_sieving,
                'caps_up_to_25':caps_up_to_25,
                'caps_other_25':caps_other_25,
                'caps_shell_25':caps_shell_25,
            }
