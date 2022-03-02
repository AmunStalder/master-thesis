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
    production             = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
    amount_of_caps         = models.IntegerField()
    conc_per_cap           = models.FloatField()
    conc_per_tab           = models.FloatField()
    amount_of_weighed_tabs = models.IntegerField()
    mass_all_tabs          = models.FloatField()
    required_mass_powder   = models.FloatField()
    weighed_mass_powder    = models.FloatField()
    caps_size              = models.FloatField(choices=CHOICES,)

    def get_absolute_url(self):
        '''
            Needs to be defined in order to redirect to a page
            upon successful filling in the form
        '''
        return reverse("capsules:functions") #kwargs={'pk':self.pk})

    def __str__(self):
        return '{}'.format(self.production.name)

    # def save(self, *args, **kwarg):
    #     self.calc = UniformityCalculator(
    #         gal_form="caps",
    #         total_mass=self.mass_20_caps_full,
    #         mass_1_caps_empty=self.mass_1_caps_empty,
    #         mass_max1=self.mass_max1,
    #         mass_max2=self.mass_max2,
    #         mass_max3=self.mass_max3,
    #         mass_min2=self.mass_min2,
    #         mass_min1=self.mass_min1,
    #         mass_min3=self.mass_min3,
    #     )
    #     self.mean                  = self.calc.mean
    #     self.diff                  = self.calc.diff
    #     self.diff_x2               = self.calc.diff_x2
    #     self.mean                  = self.calc.mean
    #     self.plus_1_diff           = self.calc.plus_1_diff
    #     self.plus_2_diff           = self.calc.plus_2_diff
    #     self.minus_1_diff          = self.calc.minus_1_diff
    #     self.minus_2_diff          = self.calc.minus_2_diff
    #     self.counter_above_1_diff  = self.calc.counter_above_1_diff
    #     self.counter_above_2_diff  = self.calc.counter_above_2_diff
    #     self.release_note          = self.calc.release_note
    #     self.uniformity_plot       = self.calc.uniformity_plot
    #     print("mean worked")
    #     super(Uniformity, self).save(*args, **kwarg)
    #
    # def get_absolute_url(self):
    #     '''
    #         Needs to be defined in order to redirect to a page
    #         upon successful filling in the form
    #     '''
    #     return reverse("capsules:detail", kwargs={'pk':self.pk})
    #
    # def __str__(self):
    #     return '{}'.format(self.production.name)
    # # @property
    # # def results(self):
    # #     self.calc = UniformityCalculator(
    # #         gal_form="caps",
    # #         total_mass=self.mass_20_caps_full,
    # #         mass_1_caps_empty=self.mass_1_caps_empty,
    # #         mass_max1=self.mass_max1,
    # #         mass_max2=self.mass_max2,
    # #         mass_max3=self.mass_max3,
    # #         mass_min2=self.mass_min2,
    # #         mass_min1=self.mass_min1,
    # #         mass_min3=self.mass_min3,
    # #     )
    # #     print(self.calc)
    # #     print("object created")
    # #     return self.calc
