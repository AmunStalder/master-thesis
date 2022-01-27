from django.db import models
from django.urls import reverse
# Create your models here.
class Uniformity(models.Model):
    caps_name           = models.CharField(max_length= 256)
    mass_1_caps_empty   = models.FloatField()
    mass_20_caps_full   = models.FloatField()
    mass_max1           = models.FloatField()
    mass_min1           = models.FloatField()

    def get_absolute_url(self):
        '''
            Needs to be defined in order to redirect to a page
            upon successful filling in the form
        '''
        return reverse("capsules:detail", kwargs={'pk':self.pk})

    @property
    def mean_content(self):
        return self.mass_20_caps_full/20 - self.mass_1_caps_empty
