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
    suppos_up_to_12     = models.IntegerField(default=1)
    suppos_other_12     = models.IntegerField(null = True)
    amount_betmg        = models.IntegerField(null = True)
    suppos_box_up_to_12 = models.IntegerField(null = True)
    substances_price    = models.FloatField(null=True)
    final_price         = models.FloatField(null = True)

    def save(self, *args, **kwarg):
        #Sum up Part I
        self.substances_price = 0
        for ingredient in Ingredient.objects.filter(production = self.production):
            self.substances_price = self.substances_price + ingredient.price_per_amount
        sum_I = self.substances_price
        #Sum up Part II.A (Zusammengesetzte Arzneimittel)
        sum_II_A = sum([
            self.suppos_up_to_12*24,
            self.suppos_other_12*18,
        ])*TAX_VALUE
        #Sum up part II.B (Betäubungsmittelzuschlag)
        self.amount_betmg = 0
        for ingredient in Ingredient.objects.filter(production = self.production.pk):
            if ingredient.substance.infos == "St":
                self.amount_betmg = self.amount_betmg + 1
        sum_II_B = self.amount_betmg*1.5*TAX_VALUE
        #Sum up part III.B (Gefässtarif)
        sum_III_B = self.suppos_box_up_to_12*.75
        self.final_price = sum_I + sum_II_A + sum_II_B + sum_III_B
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
