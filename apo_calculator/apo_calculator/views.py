from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class LandingView(TemplateView):
    template_name = 'landing.html'

class ThanksView(TemplateView):
    template_name = 'thanks.html'
