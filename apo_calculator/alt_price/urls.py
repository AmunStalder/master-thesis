from django.urls import path
from . import views

app_name = 'alt_price'
urlpatterns = [
    path('add/<int:pk>', views.ALTPriceCreateView.as_view(), name='add'),
]
