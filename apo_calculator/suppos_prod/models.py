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
    calc_date                      = models.DateTimeField(default=datetime.now, blank=True, )
    production                     = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
    amount_of_suppos               = models.IntegerField()
    # ForeignKey may be better
    active_substance_1             = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
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

        #saving ingredient (active substance, only one possible)
        ingredient = Ingredient.objects.get(production=self.production, substance = self.active_substance_1.substance)
        ingredient.target_amount = self.required_mass_active_substance
        ingredient.actual_amount = self.weighed_mass_active_substance
        #change this!!!
        ingredient.price_per_amount = 17
        ingredient.save()

        # Add Witepsol as ingredient if it does not already exist.
        try:
            excipient = Ingredient.objects.get(production=self.production, substance = Substance.objects.get(name = "Witepsol H-15 Pastillenform/en pastilles"))
        except:
            excipient = Ingredient()
        excipient.production = self.production
        excipient.substance = Substance.objects.get(name="Witepsol H-15 Pastillenform/en pastilles")
        excipient.target_amount = self.required_mass_witepsol
        excipient.actual_amount = self.weighed_mass_witepsol
        excipient.save()


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

        #this code is not checked


            # try:
            #     instance2 = production.ingredient.objects.get(pk=self.production.pk)
            # #for new calculation make new instance and prefill with production
            # #that was given by kwargs (pk=production.pk)
            # except:
            #     instance2 = Ingredient()
            #     instance2.production = Productions.objects.get(pk=self.production.pk)
            #     instance2.substance = self.active_substance_1
            #     instance2.target_amount = self.required_mass_active_substance
            #     instance2.actual_amount = self.weighed_mass_active_substance
            #     #check this
            #     instance2.price_per_amount = 17
            #
            # instance2.save()

            #Hier weitermachen: Eine neue Instanz im Ingredient mit der active substance speichern. Wenn instanz vorhaben, dann updaten, sonst erstellen.

    def __str__(self):
        return '{}'.format(self.production.name)
