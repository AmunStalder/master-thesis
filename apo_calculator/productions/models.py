from django.db import models
from django.urls import reverse
from datetime import datetime
# Create your models here.

class Productions(models.Model):
    CAPSULES = 'capsules'
    SUPPOSITORIES = 'suppositories'
    EYEDROPS = 'eyedrops'
    CHOICES = [
        (CAPSULES, 'Capsules'),
        (SUPPOSITORIES, 'Suppositories'),
        (EYEDROPS, 'Eyedrops'),
    ]
    calc_date      = models.DateTimeField(default=datetime.now, blank=True, )
    lot_nr         = models.CharField(max_length=32, unique=True,)
    galenical_form = models.CharField(max_length=16, choices=CHOICES,)
    name           = models.CharField(max_length= 256, )

    def __str__(self):
        return '{}, {}'.format(self.lot_nr, self.name)

    def get_absolute_url(self):
        '''
            Needs to be defined in order to redirect to a page
            upon successful filling in the form
        '''
        return reverse("productions:detail", kwargs={'pk':self.pk})
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
