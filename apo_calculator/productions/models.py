from django.db import models
from django.urls import reverse
from datetime import datetime
from substances.models import Substance
# Create your models here.

class Productions(models.Model):
    CAPSULES = 'capsules'
    SUPPOSITORIES = 'suppositories'
    EYEDROPS = 'eyedrops'
    CHOICES = [
        (CAPSULES, 'Capsules'),
        (SUPPOSITORIES, 'Suppositories'),
        (EYEDROPS, 'Eyedrops'),
    ]
    calc_date      = models.DateTimeField(default=datetime.now, blank=True, )
    lot_nr         = models.CharField(max_length=32, unique=True,)
    galenical_form = models.CharField(max_length=16, choices=CHOICES,)
    name           = models.CharField(max_length= 256, )

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
    production = models.ForeignKey(Productions, on_delete=models.CASCADE, )
    substance = models.ForeignKey(Substance, on_delete=models.CASCADE, )
    target_amount = models.FloatField(null=True)
    actual_amount = models.FloatField(null=True)
    price_per_amount = models.FloatField(null=True)

    def __str__(self):
        return '{}'.format(self.substance)

    def get_absolute_url(self):
        '''
            Needs to be defined in order to redirect to a page
            upon successful filling in the form
        '''
        return reverse("productions:detail", kwargs={'pk':self.production.pk})

    class Meta:
        ordering = ['substance']
        unique_together = (("production", "substance",))
