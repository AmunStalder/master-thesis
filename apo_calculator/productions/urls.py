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
    path('pdf/<int:pk>/', views.ProductionPdfView.as_view(), name='pdf'),
    path('add_ingredient/<int:pk>/', views.IngredientCreateView.as_view(), name='add_ingredient'),
    path('update_ingredient/<int:pk>/', views.IngredientUpdateView.as_view(), name='update_ingredient'),
    path('delete_ingredient/<int:pk>/', views.IngredientDeleteView.as_view(), name='delete_ingredient'),
    path('add_ambv_value/<int:pk>/', views.AMBVValueCreateView.as_view(), name='add_ambv_value'),
    path('edit_ambv_value/<int:pk>/', views.AMBVValueUpdateView.as_view(), name='edit_ambv_value'),
]
