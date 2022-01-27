from django.views.generic import TemplateView
from .forms import CapsulesUniformityOfMass
from django.views.generic.edit import FormView

# Create your views here.

#View for Capsules
class CapsulesFunctionsView(TemplateView):
    template_name = 'capsules/functions.html'
# Create your views here.

class CapsulesUniformityOfMassView(FormView):
    template_name = 'capsules/uniformity.html'
    form_class = CapsulesUniformityOfMass
    success_url = 'result'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        mass_1_caps_empty = form.cleaned_data['mass_1_caps_empty']
        mass_20_caps_full = form.cleaned_data['mass_20_caps_full']
        mass_max1 = form.cleaned_data['mass_max1']
        mass_min1 = form.cleaned_data['mass_min1']
        mean_content = mass_20_caps_full/20 - mass_1_caps_empty
        if mean_content <= 0.3:
            diff = 0.1
        else:
            diff = 0.15
        upper1 = mean_content*(1+diff)
        upper2 = mean_content*(1+2*diff)
        lower1 = mean_content*(1-diff)
        lower2 = mean_content*(1-2*diff)
        print(upper1)
        return super().form_valid(form)


class ResultView(TemplateView):
    template_name = 'capsules/result.html'
