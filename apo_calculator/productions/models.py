from django.db import models
from django.urls import reverse
from datetime import datetime
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
