from django.views.generic import DetailView
from django.http import HttpResponse, FileResponse
from django.urls import reverse_lazy
from productions import models
from django.shortcuts import get_object_or_404
# from .utils import render_to_pdf

class CapsMassBalanceView(DetailView):
    model = models.Productions
    template_name = 'caps_mass_balance/detail.html'

    #same as ProductionDetailView
    def get_context_data(self, **kwargs):
        context = super(CapsMassBalanceView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        obj = self.model.objects.get(pk=pk)
        calculated_mass_powder_mix = obj.uniformity.mean*obj.capsprod.amount_of_caps
        absolute_mass_balance = calculated_mass_powder_mix - obj.capsprod.mass_required_volume
        relative_mass_balance = absolute_mass_balance / obj.capsprod.mass_required_volume
        mass_balance_release_note = ""
        if relative_mass_balance <= 0.1 and relative_mass_balance >= -0.1:
            mass_balance_release_note = True
        else:
            mass_balance_release_note = False
        context["calculated_mass_powder_mix"] = calculated_mass_powder_mix
        context["absolute_mass_balance"] = absolute_mass_balance
        context["relative_mass_balance"] = relative_mass_balance
        context["mass_balance_release_note"] = mass_balance_release_note
        return context

    # def render_to_response(self, context, **kwargs):
    #     pdf = render_to_pdf(self.template_name, context)
    #     return HttpResponse(pdf, content_type='application/pdf')
