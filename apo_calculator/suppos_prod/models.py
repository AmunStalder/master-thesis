from django.db import models
from django.urls import reverse
from datetime import datetime
from productions.models import Productions
# Create your models here.
# class SupposProd(models.Model):
#
#     production              = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
#     amount_of_suppos        = models.IntegerField()
#     conc_per_suppo          = models.FloatField()
#     required_mass_powder    = models.FloatField()
#     weighed_mass_powder     = models.FloatField()
#     caps_size               = models.FloatField(choices=CHOICES,)
#     tara_meas_cylinder      = models.FloatField()
#     required_volume         = models.FloatField()
#     mass_required_volume    = models.FloatField()
#
#     def save(self, *args, **kwarg):
#         self.required_mass_powder  = self.amount_of_caps * self.conc_per_cap / self.conc_per_tab * self.mass_all_tabs / self.amount_of_weighed_tabs
#         super(CapsProd, self).save(*args, **kwarg)
#
#     # def get_absolute_url(self):
#
#     #     '''
#     #         Needs to be defined in order to redirect to a page
#     #         upon successful filling in the form
#     #     '''
#     #     return reverse("capsules:functions") #kwargs={'pk':self.pk})
#
#     def __str__(self):
#         return '{}'.format(self.production.name)

class SupposDisplacementValue(models.Model):
    substance       = models.CharField(max_length=64, unique=True,)
    value           = models.FloatField()

    def __str__(self):
        return self.substance
