from django.db import models
from django.urls import reverse
from datetime import datetime
from productions.models import Productions
# Create your models here.
class SupposMassBalance(models.Model):
    calc_date                         = models.DateTimeField(default=datetime.now, blank=True, )
    production                        = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
    conc_per_suppo_actual             = models.FloatField()
    conc_per_suppo_diff               = models.FloatField()
    release_note                      = models.BooleanField()

    def save(self, *args, **kwarg):
        self.conc_per_suppo_actual    = self.production.supposuniformity.mean*self.production.supposprod.conc_suppomass_per_g_actual
        self.conc_per_suppo_diff      = self.conc_per_suppo_actual/self.production.supposprod.conc_per_suppo*100 -100
        if -10 <= self.conc_per_suppo_diff <= 10:
            self.release_note = True
        else:
            self.release_note = False

        super(SupposMassBalance, self).save(*args, **kwarg)

    def __str__(self):
        return '{}'.format(self.production.name)
