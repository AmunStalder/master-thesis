from formtools.wizard.views import SessionWizardView
from . import models

# Create your views here.
# TEMPLATES = {
#     'caps_prod_form_1': 'caps_prod.html',
#     'caps_prod_form_2': 'projects/your-info-form.html',
# }
# FORMS = [
#     ('caps_prod_form_1', CapsProdForm1),
#     ('caps_prod_form_2', CapsProdForm2),
# ]


class CapsProdWizardView(SessionWizardView):
    template_name = "caps_prod/prod_form.html"

    # def get_form_instance(self, step):
    #     """
    #     Provides us with an instance of the Project Model to save on completion
    #     """
    #     if self.instance is None:
    #         self.instance = Project()
    #     return self.instance

    def done(self, form_list, **kwargs):
        """
        Save info to the DB
        """
        caps_production = self.instance
        caps_production.save()
    #
    # def get_template_names(self):
    #     """
    #     Custom templates for the different steps
    #     """
    #     return [TEMPLATES[self.steps.current]]
