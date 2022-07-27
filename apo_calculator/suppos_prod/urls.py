#we rename the views from auth to not confuse it with views.py
from django.urls import path
from . import views

app_name = 'suppos_prod'
urlpatterns = [
    path('new/<int:pk>/', views.SupposProdWizardView.as_view(), name="add_new"),
    path('edit/<int:pk>/', views.SupposProdWizardView.as_view(), name="edit"),
    path('detail/<int:pk>/', views.SupposProdDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.SupposProdDeleteView.as_view(), name='delete'),
]
