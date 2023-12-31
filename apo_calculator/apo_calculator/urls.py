"""apo_calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #get to the admin page
    path('admin/', admin.site.urls),
    #get to the homepage
    path('',views.IndexView.as_view(), name = 'index'),
    #get to landing page
    path('landing',views.LandingView.as_view(), name = 'landing'),
    #get to thanks page
    path('thanks',views.ThanksView.as_view(), name = 'thanks'),

    path('authenticate/',include('authenticate.urls', namespace ='authenticate')),
    #for default stuff
    path('authenticate/', include('django.contrib.auth.urls')),

    path('productions/', include('productions.urls', namespace = 'productions')),
    #for capsules
    path('capsules/', include('capsules.urls', namespace = 'capsules')),
    path('caps_prod/', include('caps_prod.urls', namespace = 'caps_prod')),
    path('caps_mass_balance/', include('caps_mass_balance.urls', namespace = 'caps_mass_balance')),
    path('suppos_mass_balance/', include('suppos_mass_balance.urls', namespace = 'suppos_mass_balance')),
    #for Suppositories
    path('suppositories/', include('suppositories.urls', namespace = 'suppositories')),
    path('suppos_prod/', include('suppos_prod.urls', namespace = 'suppos_prod')),
    path('substances/', include('substances.urls', namespace = 'substances')),
    path('alt_price/', include('alt_price.urls', namespace = 'alt_price')),
]
