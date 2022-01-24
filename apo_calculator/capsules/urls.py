#we rename the views from auth to not confuse it with views.py
from django.urls import path
from . import views

app_name = 'capsules'
urlpatterns = [
    #we use default auth views to create these views.
    path('functions/', views.CapsulesFunctionsView.as_view(), name='functions'),
    path('uniformity/', views.CapsulesUniformityOfMassView.as_view(), name='uniformity'),
    path('uniformity/result', views.ResultView.as_view(), name='result'),
]
