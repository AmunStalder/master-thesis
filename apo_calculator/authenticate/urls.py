#we rename the views from auth to not confuse it with views.py
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'authenticate'
urlpatterns = [
    #we use default auth views to create these views.
    path('login/', auth_views.LoginView.as_view(
    template_name='authenticate/login.html'),
    name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
