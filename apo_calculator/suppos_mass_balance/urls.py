#we rename the views from auth to not confuse it with views.py
from django.urls import path
from . import views

app_name = 'suppos_mass_balance'
urlpatterns = [
    path('detail/<int:pk>/', views.SupposMassBalanceView.as_view(), name="detail"),
    path('info/', views.SupposMassBalanceInfoView.as_view(), name="info"),
]
