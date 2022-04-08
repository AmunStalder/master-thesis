from django.db import models
from django.urls import reverse
from datetime import datetime
from productions.models import Productions
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
    calc_date                      = models.DateTimeField(default=datetime.now, blank=True, )
    production                     = models.OneToOneField(Productions, on_delete=models.CASCADE, primary_key=True)
    amount_of_caps                 = models.IntegerField()
    conc_per_cap                   = models.FloatField()
    conc_per_tab                   = models.FloatField()
    required_amount_of_tabs        = models.FloatField()
    amount_of_weighed_tabs         = models.IntegerField()
    mass_all_tabs                  = models.FloatField()
    required_mass_powder           = models.FloatField()
    weighed_mass_powder            = models.FloatField()
    caps_size                      = models.FloatField(choices=CHOICES,)
    tara_meas_cylinder             = models.FloatField()
    required_volume                = models.FloatField()
    mass_required_volume_incl_tara = models.FloatField()
    mass_required_volume           = models.FloatField()
    conc_powdermix_per_g_target    = models.FloatField()
    conc_powdermix_per_g_actual    = models.FloatField()
    conc_powdermix_per_g_diff      = models.FloatField()


    def save(self, *args, **kwarg):
        self.required_mass_powder         = self.amount_of_caps * self.conc_per_cap / self.conc_per_tab * self.mass_all_tabs / self.amount_of_weighed_tabs
        self.mass_required_volume         = self.mass_required_volume_incl_tara-self.tara_meas_cylinder
        total                             = self.amount_of_caps * self.conc_per_cap
        self.conc_powdermix_per_g_target  = total/self.mass_required_volume
        factor                            = self.weighed_mass_powder/self.required_mass_powder
        self.conc_powdermix_per_g_actual  = self.conc_powdermix_per_g_target*factor
        self.conc_powdermix_per_g_diff    = self.conc_powdermix_per_g_actual / self.conc_powdermix_per_g_target * 100 - 100
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


    # def get_absolute_url(self):

    #     '''
    #         Needs to be defined in order to redirect to a page
    #         upon successful filling in the form
    #     '''
    #     return reverse("capsules:functions") #kwargs={'pk':self.pk})

    def __str__(self):
        return '{}'.format(self.production.name)
