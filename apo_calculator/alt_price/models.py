from django.db import models
from django.urls import reverse
from datetime import datetime
from django.db.models import Count
from productions.models import Productions, Ingredient
from apo_calculator.utils import myround
# Create your models here.
TAX_VALUE = 1.08
class ALTPrice(models.Model):
    production          = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
    suppos_up_to_12     = models.IntegerField(null = True)
    suppos_other_12     = models.IntegerField(null = True)
    caps_mixing         = models.IntegerField(null = True)
    caps_sieving        = models.IntegerField(null = True)
    caps_up_to_25       = models.IntegerField(null = True, default=1)
    caps_other_25       = models.IntegerField(null = True)
    caps_shell_25       = models.IntegerField(null = True)
    amount_betmg        = models.IntegerField(null = True)
    suppos_box_up_to_12 = models.IntegerField(null = True, default=0)
    pulvis_50_ml        = models.IntegerField(null = True)
    pulvis_100_ml       = models.IntegerField(null = True)
    substances_price    = models.FloatField(null=True)
    manual_price        = models.FloatField(null=True)
    betmg_price         = models.FloatField(null=True)
    packaging_price     = models.FloatField(null=True)
    final_price         = models.FloatField(null = True)

    def save(self, *args, **kwarg):
        #Sum up Part I
        self.substances_price = 0
        for ingredient in Ingredient.objects.filter(production = self.production):
            self.substances_price = self.substances_price + ingredient.price_per_amount
        self.substances_price = myround(self.substances_price)
        #Sum up part II.B (Betäubungsmittelzuschlag)
        self.amount_betmg = 0
        for ingredient in Ingredient.objects.filter(production = self.production.pk):
            if ingredient.substance:
                if ingredient.substance.infos == "St":
                    self.amount_betmg = self.amount_betmg + 1
        self.betmg_price = self.amount_betmg*1.5*TAX_VALUE
        if self.production.galenical_form == "capsules":
            #Sum up Part II.A (Zusammengesetzte Arzneimittel)
            self.manual_price = sum([
                self.caps_mixing*12,
                self.caps_sieving*12,
                self.caps_up_to_25*24,
                self.caps_other_25*12,
            ])*TAX_VALUE
            #Sum up part III.B (Gefässtarif)
            caps_shell_price = 0
            if self.production.capsprod.caps_size in [0.78, 0.5, 0.37, 0.3]:
                caps_shell_price = 1.7
            elif self.production.capsprod.caps_size in [0.21, 0.1]:
                caps_shell_price = 3.1
            else:
                caps_shell_price = 9.1
            self.packaging_price = self.pulvis_50_ml*1.2 + self.pulvis_100_ml*1.3 + self.caps_shell_25*caps_shell_price
        if self.production.galenical_form == "suppositories":
            #Sum up Part II.A (Zusammengesetzte Arzneimittel)
            self.manual_price = sum([
                self.suppos_up_to_12*24,
                self.suppos_other_12*18,
            ])*TAX_VALUE
            #Sum up part III.B (Gefässtarif)
            self.packaging_price = self.suppos_box_up_to_12*.75
        self.final_price = self.substances_price + self.manual_price + self.betmg_price + self.packaging_price
        self.final_price = myround(self.final_price)
        super(ALTPrice, self).save(*args, **kwarg)
        #Then update the values for the ingredients, in case something has changed



    def __str__(self):
        return 'ALT price for {}'.format(self.production.name)

    def get_absolute_url(self):
        '''
            Needs to be defined in order to redirect to a page
            upon successful filling in the form
        '''
        return reverse("productions:detail", kwargs={'pk':self.production.pk})
