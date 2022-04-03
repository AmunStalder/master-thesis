from django.db import models
from django.urls import reverse
from datetime import datetime
from productions.models import Productions

class SupposDisplacementValue(models.Model):
    substance       = models.CharField(max_length=64,)
    value           = models.FloatField()

    def __str__(self):
        return self.substance

class SupposProd(models.Model):
    production              = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
    amount_of_suppos        = models.IntegerField()
    active_substance_1      = models.ForeignKey(SupposDisplacementValue, on_delete=models.CASCADE)
    conc_per_suppo          = models.FloatField()
    calibration_value       = models.FloatField()
    required_mass_active_substance = models.FloatField()
    weighed_mass_active_substance = models.FloatField()
    required_mass_witepsol = models.FloatField()
    weighed_mass_witepsol = models.FloatField()


    def save(self, *args, **kwarg):
        super(SupposProd, self).save(*args, **kwarg)

    def __str__(self):
        return '{}'.format(self.production.name)
