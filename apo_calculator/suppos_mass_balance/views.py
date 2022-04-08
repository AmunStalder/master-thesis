from django.views.generic import DetailView
from django.http import HttpResponse, FileResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from productions import models
# Create your views here.

class SupposMassBalanceView(DetailView):
    model = models.Productions
    template_name = 'suppos_mass_balance/detail.html'
