from django.db import models
from django.urls import reverse
from datetime import datetime
from substances.models import Substance, FinishedMedicinalProduct
from apo_calculator.utils import price_per_ingredient
import math
# Create your models here.

class Productions(models.Model):
    CAPSULES = 'capsules'
    SUPPOSITORIES = 'suppositories'
    CHOICES = [
        (CAPSULES, 'Capsules'),
        (SUPPOSITORIES, 'Suppositories'),
    ]
    calc_date      = models.DateTimeField(default=datetime.now, blank=True, )
    lot_nr         = models.CharField(max_length=32, unique=True,)
    galenical_form = models.CharField(max_length=16, choices=CHOICES,)
    name           = models.CharField(max_length= 256, )
    dose_units     = models.IntegerField()
    dose_units_incl_excess = models.IntegerField()
    release_note   = models.BooleanField(null = True)

    #Update Ingredients if Production is updated
    def save(self, *args, **kwarg):
        #First save the instance of Productions
        super(Productions, self).save(*args, **kwarg)
        #Then update the values for the ingredients, in case something has changed
        for ingredient in Ingredient.objects.filter(production = Productions.objects.get(pk = self.pk)):
            ingredient.save()


    def __str__(self):
        return '{}, {}'.format(self.lot_nr, self.name)

    def get_absolute_url(self):
        '''
            Needs to be defined in order to redirect to a page
            upon successful filling in the form
        '''
        return reverse("productions:detail", kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-calc_date']

class Ingredient(models.Model):
    yes   = True
    no   = False

    CHOICES = [
        (yes, 'Yes'),
        (no, 'No'),
    ]
    production             = models.ForeignKey(Productions, on_delete=models.CASCADE, )
    substance              = models.ForeignKey(Substance, on_delete=models.CASCADE, null=True)
    fmp                    = models.ForeignKey(FinishedMedicinalProduct, on_delete=models.CASCADE, null=True)
    conc_per_dose_unit     = models.FloatField(null=True, blank=False)
    conc_per_bulk          = models.FloatField(null=True, blank=False)
    required_amount_of_tabs = models.FloatField(null=True, blank=False)
    required_amount_of_tabs_incl_excess = models.IntegerField(null=True, blank=False)
    weight_tabs_incl_excess= models.FloatField(null=True, blank=False)
    target_amount_for_bulk = models.FloatField(null=True)
    actual_amount_for_bulk = models.FloatField(null=True)
    diff_amount_for_bulk   = models.FloatField(null=True)
    is_filler_excipient    = models.BooleanField(choices = CHOICES, null = True, default=False)
    price_per_amount       = models.FloatField(null=True)

    def save(self, *args, **kwarg):
        if self.production.galenical_form == "suppositories" and self.substance.name != 'Witepsol H-15 Pastillenform/en pastilles':
            self.target_amount_for_bulk = self.production.dose_units_incl_excess * self.conc_per_dose_unit / 1000
        elif self.production.galenical_form == "capsules" and self.is_filler_excipient == False:
            self.conc_per_bulk = self.production.dose_units_incl_excess * self.conc_per_dose_unit / 1000
            self.required_amount_of_tabs = self.conc_per_bulk * 1000 / (self.fmp.conc_per_dose_unit_mg)
            if self.required_amount_of_tabs_incl_excess:
                pass
            else:
                self.required_amount_of_tabs_incl_excess = math.ceil(self.required_amount_of_tabs*1.1)
        else:
            pass

        if self.actual_amount_for_bulk is not None and self.target_amount_for_bulk is not None:
            print(17)
            self.diff_amount_for_bulk = (self.actual_amount_for_bulk-self.target_amount_for_bulk) / self.target_amount_for_bulk * 100
        if self.actual_amount_for_bulk is not None and self.substance:
            self.price_per_amount = price_per_ingredient(self.actual_amount_for_bulk, self.substance)
        if self.fmp:
            self.price_per_amount = self.fmp.price_chf
        else:
            pass
        super(Ingredient, self).save(*args, **kwarg)


    def __str__(self):
        if self.substance:
            return '{}'.format(self.substance)
        else:
            return '{}'.format(self.fmp)

    def get_absolute_url(self):
        '''
            Needs to be defined in order to redirect to a page
            upon successful filling in the form
        '''
        return reverse("productions:detail", kwargs={'pk':self.production.pk})

    class Meta:
        ordering = ['substance']
        unique_together = (("production", "substance",))

class AMBVValue(models.Model):
    CONTRACT_MANUF_CHOICES = [
        (5.,'exclusively contract manufacture'),
        (4.,'mainly contract manufacture (ratio: around 2:1)'),
        (3.,'balanced (ratio: around 1:1)'),
        (2.,'mainly for own customers (ratio: around 1:2)'),
        (0.2,'exclusively for own customers'),
        ]
    MANUF_PROCESS_CHOICES = [
        (5,'aseptic manufacture'),
        (4,'manufacture with terminal sterilisation'),
        (3,'dissolving and mixing'),
        (2,'diluting'),
        (1,'filling of non-sterile dosage forms'),
        ]
    INHERENT_RISK_CHOICES = [
        (5,'high risk'),
        (3,'medium risk'),
        (1,'low risk'),
        ]
    ROA_CHOICES = [
        (5.,'parenteral administration'),
        (4.000001,'ophthalmological administration in surgery or for traumatic injuries'),
        (4.000002,'inhaled administration'),
        (4.000003,'enteral or topical administration with requirements for sterility'),
        (3.,'enteral administration'),
        (1.000001,'ophthalmological administration in the uninjured eye'),
        (1.000002,'topical administration'),
        ]
    AMOUNT_CHOICES = [
        ('a. liquid dosage forms in standard pack units or application units in litres', (
           (5, 'more than 2,000'),
           (4, '1000–2000'),
           (3, '500–999'),
           (2, '100–499'),
           (1, 'less than 100'),
       )
        ),
       ('b. solid dosage forms, number of units', (
           (5, 'more than 120,000'),
           (4, '60,000–120,000'),
           (3, '30,000–59,999'),
           (2, '6,000–29,999'),
           (1, 'less than 6000'),
       )
        ),
       ('c. semi-solid dosage forms (suppositories), number of units', (
           (5, 'more than 40,000'),
           (4, '20,000–40,000'),
           (3, '10,000–19,999'),
           (2, '2000–9999'),
           (1, 'less than 2000'),
       )
        ),
       ('d. semi-solid dosage forms (ointments, creams, etc.) in grams', (
           (5, 'more than 200,000'),
           (4, '100,000–200,000'),
           (3, '50,000–99,999'),
           (2, '10,000–49,999'),
           (1, 'less than 10,000'),
       )
        ),
       ('e. eye drops in litres', (
           (5, 'more than 200'),
           (4, '100–200'),
           (3, '50–99'),
           (2, '10–49'),
           (1, 'less than 10'),
       )
        ),
        ]


    production     = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
    yearly_amount  = models.IntegerField(choices=AMOUNT_CHOICES)
    roa            = models.FloatField(choices = ROA_CHOICES)
    inherent_risk  = models.IntegerField(choices = INHERENT_RISK_CHOICES)
    manuf_process  = models.IntegerField(choices = MANUF_PROCESS_CHOICES)
    contract_manuf = models.FloatField(choices = CONTRACT_MANUF_CHOICES)
    value          = models.FloatField()

    def save(self, *args, **kwarg):
        self.value = round(self.yearly_amount * self.roa * self.inherent_risk * self.manuf_process * self.contract_manuf,2)
        super(AMBVValue, self).save(*args, **kwarg)

    def __str__(self):
        return '{}'.format(self.production)

    def get_absolute_url(self):
        '''
            Needs to be defined in order to redirect to a page
            upon successful filling in the form
        '''
        return reverse("productions:detail", kwargs={'pk':self.production.pk})
