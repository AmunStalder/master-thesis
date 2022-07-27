from django.db import models
from django.urls import reverse
from datetime import datetime
from productions.models import Productions, Ingredient
from suppos_mass_balance.models import SupposMassBalance
from substances.models import Substance

class SupposDisplacementValue(models.Model):
    substance       = models.CharField(max_length=64,)
    value           = models.FloatField()

    def __str__(self):
        return self.substance

class SupposProd(models.Model):
    calc_date                       = models.DateTimeField(default=datetime.now, blank=True, )
    production                      = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
    calib_value_suppo_mould         = models.FloatField()
    tara_pouring_bowl               = models.FloatField()
    #weighed
    actual_mass_bulk_incl_tara      = models.FloatField()
    #weighed excl. tara
    actual_mass_bulk                = models.FloatField()

    #weighed / target
    diff_actual_mass_bulk           = models.FloatField()
    #calculated
    target_mass_bulk                = models.FloatField()
    #calculated from individual weights of ingredients.
    calculated_mass_bulk            = models.FloatField()
    #calculated / target
    diff_calculated_mass_bulk       = models.FloatField()
    release_note                    = models.BooleanField()


    def save(self, *args, **kwarg):
        self.target_mass_bulk = 0
        self.calculated_mass_bulk = 0
        for ingredient in Ingredient.objects.filter(production = self.production):
            self.target_mass_bulk = self.target_mass_bulk + ingredient.target_amount_for_bulk
            self.calculated_mass_bulk = self.calculated_mass_bulk + ingredient.actual_amount_for_bulk
        self.actual_mass_bulk = self.actual_mass_bulk_incl_tara - self.tara_pouring_bowl
        self.diff_calculated_mass_bulk = (self.calculated_mass_bulk-self.target_mass_bulk)/self.target_mass_bulk*100
        self.diff_actual_mass_bulk =  (self.actual_mass_bulk-self.target_mass_bulk)/self.target_mass_bulk*100
        for ingredient in Ingredient.objects.filter(production = self.production):
            if abs(ingredient.diff_amount_for_bulk) <= 10:
                self.release_note = True
            else:
                self.release_note = False
                break

        if self.release_note and self.diff_calculated_mass_bulk <= 10:
            self.release_note = True
        else:
            self.release_note = False

        super(SupposProd, self).save(*args, **kwarg)

        if hasattr(self.production, 'supposuniformity'):
            try:
                SMB = production.supposmassbalance.objects.get(pk=self.production.pk)
            #for new calculation make new instance and prefill with production
            #that was given by kwargs (pk=production.pk)
            except:
                SMB = SupposMassBalance()
                SMB.production = Productions.objects.get(pk=self.production.pk)

            SMB.save()

    def __str__(self):
        return '{}'.format(self.production.name)
