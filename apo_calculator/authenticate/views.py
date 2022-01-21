from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    #When form is vorrectly filled in, and submit is clicked, we go to login
    success_url = reverse_lazy('login')
    template_name = 'authenticate/signup.html'
