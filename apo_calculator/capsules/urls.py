#we rename the views from auth to not confuse it with views.py
from django.urls import path
from . import views

app_name = 'capsules'
urlpatterns = [
    path('uniformity/<int:pk>/', views.CapsUnifCreateView.as_view(), name='uniformity'),
    path('uniformity/detail/<int:pk>/', views.CapsUnifDetailView.as_view(), name='detail'),
    path('uniformity/update/<int:pk>/', views.CapsUnifUpdateView.as_view(), name='update'),
    path('uniformity/delete/<int:pk>/', views.CapsUnifDeleteView.as_view(), name='delete'),
    path('info/', views.CapsInfoView.as_view(), name='info'),

]
