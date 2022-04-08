from django.db import models

# Create your models here.
class EyeDropsFreezingPointDepressionValue(models.Model):
    substance       = models.CharField(max_length=64,)
    value           = models.FloatField()

    def __str__(self):
        return self.substance
