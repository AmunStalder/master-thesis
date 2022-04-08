from django.db import models
from django.urls import reverse
from datetime import datetime
from productions.models import Productions
from suppos_mass_balance.models import SupposMassBalance

class SupposDisplacementValue(models.Model):
    substance       = models.CharField(max_length=64,)
    value           = models.FloatField()

    def __str__(self):
        return self.substance

class SupposProd(models.Model):
    calc_date                      = models.DateTimeField(default=datetime.now, blank=True, )
    production                     = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
    amount_of_suppos               = models.IntegerField()
    active_substance_1             = models.ForeignKey(SupposDisplacementValue, on_delete=models.CASCADE)
    conc_per_suppo                 = models.FloatField()
    calibration_value              = models.FloatField()
    required_mass_active_substance = models.FloatField()
    weighed_mass_active_substance  = models.FloatField()
    required_mass_witepsol         = models.FloatField()
    weighed_mass_witepsol          = models.FloatField()
    mass_suppomass_actual          = models.FloatField()
    conc_suppomass_per_g_target    = models.FloatField()
    conc_suppomass_per_g_actual    = models.FloatField()
    conc_suppomass_per_g_diff      = models.FloatField()


    def save(self, *args, **kwarg):
        self.mass_suppomass_actual       = self.weighed_mass_witepsol + self.weighed_mass_active_substance/1000
        self.conc_suppomass_per_g_target = self.required_mass_active_substance /(self.required_mass_active_substance+self.required_mass_witepsol*1000)*1000
        self.conc_suppomass_per_g_actual = self.weighed_mass_active_substance / (self.weighed_mass_active_substance + self.weighed_mass_witepsol*1000)*1000
        self.conc_suppomass_per_g_diff   = self.conc_suppomass_per_g_actual / self.conc_suppomass_per_g_target * 100 - 100
        super(SupposProd, self).save(*args, **kwarg)
        if hasattr(self.production, 'supposuniformity'):
            try:
                instance = production.supposmassbalance.objects.get(pk=self.production.pk)
            #for new calculation make new instance and prefill with production
            #that was given by kwargs (pk=production.pk)
            except:
                instance = SupposMassBalance()
                instance.production = Productions.objects.get(pk=self.production.pk)

            instance.save()

    def __str__(self):
        return '{}'.format(self.production.name)
