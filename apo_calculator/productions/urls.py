from django.urls import path
from . import views

app_name = 'productions'
urlpatterns = [
    path('functions/', views.ProductionFuncView.as_view(), name='functions'),
    path('create/', views.ProductionCreateView.as_view(), name='create'),
    path('list/', views.ProductionListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.ProductionDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.ProductionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProductionDeleteView.as_view(), name='delete'),
    path('pdf/<int:pk>/', views.CapsPdfView.as_view(), name='pdf'),
]
