from django.views.generic import DetailView, TemplateView
from django.http import HttpResponse, FileResponse
from django.urls import reverse_lazy
from productions import models
from django.shortcuts import get_object_or_404
# from .utils import render_to_pdf

class CapsMassBalanceView(DetailView):
    model = models.Productions
    template_name = 'caps_mass_balance/detail.html'

class CapsMassBalanceInfoView(TemplateView):
    model = models.Productions
    template_name = "caps_mass_balance/info.html"
