#we rename the views from auth to not confuse it with views.py
from django.urls import path
from . import views

app_name = 'caps_prod'
urlpatterns = [
    path('new/<int:pk>/', views.CapsProdWizardView.as_view(), name="add_new"),
    path('edit/<int:pk>/', views.CapsProdWizardView.as_view(), name="edit"),
    path('detail/<int:pk>/', views.CapsProdDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.CapsProdDeleteView.as_view(), name='delete'),
]
