from django.urls import path
from . import views

app_name = 'substances'
urlpatterns = [
    path('list/', views.SubstanceListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.SubstanceDetailView.as_view(), name='detail'),
    path('FMP/create/', views.FinishedMedicinalProductCreateView.as_view(), name='fmp-create'),
    path('FMP/list/', views.FinishedMedicinalProductListView.as_view(), name='fmp-list'),
    path('FMP/detail/<int:pk>/', views.FinishedMedicinalProductDetailView.as_view(), name='fmp-detail'),
    path('FMP/update/<int:pk>/', views.FinishedMedicinalProductUpdateView.as_view(), name='fmp-update'),
    path('FMP/delete/<int:pk>/', views.FinishedMedicinalProductDeleteView.as_view(), name='fmp-delete'),
]
