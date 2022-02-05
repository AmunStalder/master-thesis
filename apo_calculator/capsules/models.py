from django.db import models
from django.urls import reverse
from datetime import datetime
from .calculator import UniformityCalculator
# Create your models here.
class Uniformity(models.Model):
    calc_date           = models.DateTimeField(default=datetime.now, blank=True, )
    caps_name           = models.CharField(max_length= 256)
    mass_1_caps_empty   = models.FloatField()
    mass_20_caps_full   = models.FloatField()
    mass_max1           = models.FloatField()
    mass_max2           = models.FloatField()
    mass_max3           = models.FloatField()
    mass_min1           = models.FloatField()
    mass_min2           = models.FloatField()
    mass_min3           = models.FloatField()
    #ForeignKey here

    def get_absolute_url(self):
        '''
            Needs to be defined in order to redirect to a page
            upon successful filling in the form
        '''
        return reverse("capsules:detail", kwargs={'pk':self.pk})

    @property
    def results(self):
        calc = UniformityCalculator(
            gal_form="caps",
            total_mass=self.mass_20_caps_full,
            mass_1_caps_empty=self.mass_1_caps_empty,
            mass_max1=self.mass_max1,
            mass_max2=self.mass_max2,
            mass_max3=self.mass_max3,
            mass_min2=self.mass_min2,
            mass_min1=self.mass_min1,
            mass_min3=self.mass_min3,
        )
        results = calc.calculate()
        print(results)
        return results
