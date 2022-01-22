#we rename the views from auth to not confuse it with views.py
from django.urls import path
from . import views

app_name = 'suppositories'
urlpatterns = [
    #we use default auth views to create these views.
    path('functions/', views.SuppositoriesFunctionsView.as_view(), name='functions'),
]
