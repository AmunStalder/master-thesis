from django.db import models
from django.urls import reverse
from datetime import datetime
from productions.models import Productions
# Create your models here.
class CapsMassBalance(models.Model):
    calc_date                   = models.DateTimeField(default=datetime.now, blank=True, )
    production                  = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
    calculated_mass_powder_mix  = models.FloatField(null=True)
    absolute_mass_balance       = models.FloatField(null=True)
    diff_mass_balance           = models.FloatField(null=True)
    release_note                = models.BooleanField(null=True)

    def save(self, *args, **kwarg):
        #self.production                  = Productions.objects.get(pk=self.pk)
        self.calculated_mass_powder_mix  = self.production.uniformity.mean*self.production.dose_units/1000
        self.absolute_mass_balance       = self.calculated_mass_powder_mix - self.production.capsprod.mass_required_volume
        self.diff_mass_balance           = (self.absolute_mass_balance / self.production.capsprod.mass_required_volume) * 100
        if -10 <= self.diff_mass_balance <= 10:
            self.release_note = True
        else:
            self.release_note = False

        super(CapsMassBalance, self).save(*args, **kwarg)

    def __str__(self):
        return '{}'.format(self.production.name)
