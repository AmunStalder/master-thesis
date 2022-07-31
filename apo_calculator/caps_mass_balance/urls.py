from django.urls import path
from . import views

app_name = 'caps_mass_balance'
urlpatterns = [
    path('detail/<int:pk>/', views.CapsMassBalanceView.as_view(), name="detail"),
    path('info/', views.CapsMassBalanceInfoView.as_view(), name="info"),
]
