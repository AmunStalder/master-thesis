from django.db import models
from django.urls import reverse
# Create your models here.
class Substance(models.Model):
    #nALT = not part of Arzneimittelliste mit Tarif
    nALT   = "nALT"
    L      = "L"
    #BetmG = Betäubungsmittel
    St     = "St"

    CHOICES = [
        (nALT, 'Non-ALT substance'),
        (L, 'Limited'),
        (St, 'Narcotic'),
    ]

    name                      = models.CharField(max_length=128, blank=False, null=False, unique=True)
    infos                     = models.CharField(max_length=32, choices=CHOICES, blank=True, null=False)
    freezing_point_depression = models.FloatField(blank=True, null=True)
    displacement_value        = models.FloatField(blank=True, null=True)
    price_0_001_g_ml          = models.FloatField(blank=True, null=True)
    price_0_01_g_ml           = models.FloatField(blank=True, null=True)
    price_0_1_g_ml            = models.FloatField(blank=True, null=True)
    price_1_g_ml              = models.FloatField(blank=True, null=True)
    price_10_g_ml             = models.FloatField(blank=True, null=True)
    price_100_g_ml            = models.FloatField(blank=True, null=True)
    price_500_g_ml            = models.FloatField(blank=True, null=True)
    price_1000_g_ml           = models.FloatField(blank=True, null=True)


    def __str__(self):
        return self.name

class FinishedMedicinalProduct(models.Model):
    tablets   = "tablets"

    CHOICES = [
        (tablets, 'Tablets'),
    ]
    name                      = models.CharField(max_length=128, blank=False, null=False, unique=True)
    main_ingredient           = models.CharField(max_length=128, blank=False, null=False)
    manufacturer              = models.CharField(max_length=128, blank=False, null=False)
    galenical_form            = models.CharField(max_length=32, choices=CHOICES, blank=True, null=False)
    dose_units_per_package    = models.IntegerField()
    conc_per_dose_unit_mg     = models.FloatField()
    price_chf                 = models.FloatField()



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        '''
            Needs to be defined in order to redirect to a page
            upon successful filling in the form
        '''
        return reverse("substances:fmp-detail", kwargs={'pk':self.pk})
