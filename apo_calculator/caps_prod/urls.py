#we rename the views from auth to not confuse it with views.py
from django.urls import path
from . import views
from .forms import CapsProdForm1, CapsProdForm2

app_name = 'caps_prod'
urlpatterns = [
    path('', views.CapsProdWizardView.as_view([CapsProdForm1, CapsProdForm2]), name="add_new"),
]
