#we rename the views from auth to not confuse it with views.py
from django.urls import path
from . import views

app_name = 'capsules'
urlpatterns = [
    #we use default auth views to create these views.
    path('functions/', views.CapsFuncView.as_view(), name='functions'),
    path('uniformity/<int:pk>/', views.CapsUnifCreateView.as_view(), name='uniformity'),
    # path('uniformity/result', views.ResultView.as_view(), name='result'),
    path('uniformity/list/', views.CapsUnifListView.as_view(), name='list'),
    path('uniformity/detail/<int:pk>/', views.CapsUnifDetailView.as_view(), name='detail'),
    path('uniformity/pdf/<int:pk>/', views.CapsUnifPdfView.as_view(), name='pdf'),
    path('uniformity/update/<int:pk>/', views.CapsUnifUpdateView.as_view(), name='update'),
    path('uniformity/delete/<int:pk>/', views.CapsUnifDeleteView.as_view(), name='delete'),
    # path('uniformity/pdf/<int:pk>/', views.pdf_view, name='pdf')
]
