from django.db import models
from django.urls import reverse
from datetime import datetime
from productions.models import Productions
# Create your models here.
class SupposMassBalance(models.Model):
    calc_date                         = models.DateTimeField(default=datetime.now, blank=True, )
    production                        = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
    theoretical_mass_bulk             = models.FloatField()
    mass_balance_diff                 = models.FloatField()
    release_note                      = models.BooleanField()

    def save(self, *args, **kwarg):
        self.theoretical_mass_bulk    = self.production.supposuniformity.mean * self.production.dose_units_incl_excess
        self.mass_balance_diff        = (self.theoretical_mass_bulk-self.production.supposprod.target_mass_bulk)/self.production.supposprod.calculated_mass_bulk*100
        if -10 <= self.mass_balance_diff <= 10:
            self.release_note = True
        else:
            self.release_note = False

        super(SupposMassBalance, self).save(*args, **kwarg)

    def __str__(self):
        return '{}'.format(self.production.name)
