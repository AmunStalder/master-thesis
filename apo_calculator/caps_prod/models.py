from django.db import models
from django.urls import reverse
from datetime import datetime
from productions.models import Productions, Ingredient
from caps_mass_balance.models import CapsMassBalance
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
    production                     = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
    caps_size                      = models.FloatField(choices=CHOICES,)
    tara_meas_cylinder             = models.FloatField()
    required_volume                = models.FloatField()
    mass_required_volume_incl_tara = models.FloatField()
    mass_required_volume           = models.FloatField()
    release_note                   = models.FloatField()
    def save(self, *args, **kwarg):
        for ingredient in Ingredient.objects.filter(production = self.production, is_filler_excipient = False):
            if abs(ingredient.diff_amount_for_bulk) <= 10:
                self.release_note = True
            else:
                self.release_note = False
                break
        super(CapsProd, self).save(*args, **kwarg)

        if hasattr(self.production, 'uniformity'):
            try:
                instance = production.capsmassbalance.objects.get(pk=self.production.pk)
            #for new calculation make new instance and prefill with production
            #that was given by kwargs (pk=production.pk)
            except:
                instance = CapsMassBalance()
                instance.production = Productions.objects.get(pk=self.production.pk)

            instance.save()

    def __str__(self):
        return '{}'.format(self.production.name)
