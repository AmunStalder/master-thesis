from django.core.management.base import BaseCommand
import pandas as pd
from suppos_prod.models import SupposDisplacementValue

#tutorial: https://www.youtube.com/watch?v=TL6qLQoJLsw&ab_channel=SyedZano
#source: https://dacnrf3.pharmazeutische-zeitung.de/avoxa-xaveropp/dac-nrf/start.xav?ident=79771580b2ac844d679608a001f80edb&brand=Lizenziert+zur+ausschlie%C3%9Flichen+Nutzung+durch+Klus-Apotheke%2C+8032+Z%C3%BCrich&user=klusapo&backlink=https%3A%2F%2Fdacnrf.pharmazeutische-zeitung.de%2Findex.php%3Fid%3Dsuchen%26doctronicreturn%3D1%26inputSuchen%3Dverdr%C3%A4ngungsfaktor%26andorSuchen%3D%26bereichSuchen%3D&qn=external&te0=Verdr%C3%A4ngungsfaktor&cr0=Anywhere&te1=%22dac-nrf_anlage-f%22&cr1=externalID&up2=all#__dac-nrf__%2F%2F*%5B%40attr_id%3D%27dac-nrf_anlage-f%27%5D__1648318332115

# Ammoniumbituminosulfonat/Wasser-Mischung 1:1 and Progesteron have been removed form the database
#run python manage.py updatemodels to populate database
class Command(BaseCommand):
    help = 'import booms'
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #Database connections
        #reding in displacementvalues
        df = pd.read_csv('SupposDisplacementValues.csv', sep=';')
        for substance, value in zip(df.substance,df.value):
            #replacing comma with dot
            value = value.replace(",",".")
            # change from string to float
            value = float(value)
            #create model instance
            model = SupposDisplacementValue(substance=substance, value=value)
            #save model instance
            model.save()
