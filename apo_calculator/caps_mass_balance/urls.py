#we rename the views from auth to not confuse it with views.py
from django.urls import path
from . import views

app_name = 'caps_mass_balance'
urlpatterns = [
    path('detail/<int:pk>/', views.CapsMassBalanceView.as_view(), name="detail"),
    # path('edit/<int:pk>/', views.CapsProdWizardView.as_view([CapsProdForm1, CapsProdForm2, CapsProdForm3, CapsProdForm4]), name="edit"),
]
