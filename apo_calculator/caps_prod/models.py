from django.db import models
from django.urls import reverse
from datetime import datetime
from productions.models import Productions
# Create your models here.
class CapsProd(models.Model):
    OOO   = 1.37
    OO    = 0.91
    O     = 0.78
    one   = 0.5
    two   = 0.37
    three = 0.3
    four  = 0.21
    five  = 0.1

    CHOICES = [
        (OOO, '000'),
        (OO, '00'),
        (O, '0'),
        (one, '1'),
        (two, '2'),
        (three, '3'),
        (four, '4'),
        (five, '5'),
    ]
    production              = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
    amount_of_caps          = models.IntegerField()
    conc_per_cap            = models.FloatField()
    conc_per_tab            = models.FloatField()
    required_amount_of_tabs = models.FloatField()
    amount_of_weighed_tabs  = models.IntegerField()
    mass_all_tabs           = models.FloatField()
    required_mass_powder    = models.FloatField()
    weighed_mass_powder     = models.FloatField()
    caps_size               = models.FloatField(choices=CHOICES,)

    def save(self, *args, **kwarg):
        self.required_mass_powder  = self.amount_of_caps * self.conc_per_cap / self.conc_per_tab * self.mass_all_tabs / self.amount_of_weighed_tabs
        super(CapsProd, self).save(*args, **kwarg)

    def get_absolute_url(self):
        '''
            Needs to be defined in order to redirect to a page
            upon successful filling in the form
        '''
        return reverse("capsules:functions") #kwargs={'pk':self.pk})

    def __str__(self):
        return '{}'.format(self.production.name)
