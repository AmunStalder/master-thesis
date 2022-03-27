#we rename the views from auth to not confuse it with views.py
from django.urls import path
from . import views
from .forms import CapsProdForm1, CapsProdForm2, CapsProdForm3, CapsProdForm4

app_name = 'caps_prod'
urlpatterns = [
    path('new/<int:pk>/', views.CapsProdWizardView.as_view([CapsProdForm1, CapsProdForm2, CapsProdForm3, CapsProdForm4]), name="add_new"),
    path('edit/<int:pk>/', views.CapsProdWizardView.as_view([CapsProdForm1, CapsProdForm2, CapsProdForm3, CapsProdForm4]), name="edit"),
    path('detail/<int:pk>/', views.CapsProdDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.CapsProdDeleteView.as_view(), name='delete'),
]
