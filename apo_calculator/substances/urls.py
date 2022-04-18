from django.urls import path
from . import views

app_name = 'substances'
urlpatterns = [
    path('list/', views.SubstanceListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.SubstanceDetailView.as_view(), name='detail'),
]
