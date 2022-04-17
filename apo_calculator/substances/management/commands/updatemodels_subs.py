from django.core.management.base import BaseCommand
import pandas as pd
import numpy as np
from substances.models import Substance

#tutorial: https://www.youtube.com/watch?v=TL6qLQoJLsw&ab_channel=SyedZano

#source displacement_value: https://dacnrf3.pharmazeutische-zeitung.de/avoxa-xaveropp/dac-nrf/start.xav?ident=79771580b2ac844d679608a001f80edb&brand=Lizenziert+zur+ausschlie%C3%9Flichen+Nutzung+durch+Klus-Apotheke%2C+8032+Z%C3%BCrich&user=klusapo&backlink=https%3A%2F%2Fdacnrf.pharmazeutische-zeitung.de%2Findex.php%3Fid%3Dsuchen%26doctronicreturn%3D1%26inputSuchen%3Dverdr%C3%A4ngungsfaktor%26andorSuchen%3D%26bereichSuchen%3D&qn=external&te0=Verdr%C3%A4ngungsfaktor&cr0=Anywhere&te1=%22dac-nrf_anlage-f%22&cr1=externalID&up2=all#__dac-nrf__%2F%2F*%5B%40attr_id%3D%27dac-nrf_anlage-f%27%5D__1648318332115

#source freezing_point_depression:

#source prices:


# Ammoniumbituminosulfonat/Wasser-Mischung 1:1 and Progesteron have been removed form the database
#run python manage.py updatemodels_subs to populate database
class Command(BaseCommand):
    help = 'import booms'
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #Database connections
        #reding in displacementvalues
        df = pd.read_csv('Substances.csv', sep=';')
        #turning NaN values of "info" column into empty string, because CharField in Substance model does not allow NaN values
        df["infos"] = df["infos"].replace(np.nan,'',regex=True)
        for name, infos, freezing_point_depression, displacement_value, price_0_001_g_ml, price_0_01_g_ml, price_0_1_g_ml, price_1_g_ml, price_10_g_ml, price_100_g_ml, price_500_g_ml, price_1000_g_ml in zip(df.name, df.infos, df.freezing_point_depression, df.displacement_value, df.price_0_001_g_ml, df.price_0_01_g_ml, df.price_0_1_g_ml, df.price_1_g_ml, df.price_10_g_ml, df.price_100_g_ml, df.price_500_g_ml, df.price_1000_g_ml):
            #create model instance

            model = Substance(
                name=name,
                infos=infos,
                freezing_point_depression=float(freezing_point_depression),
                displacement_value =float(displacement_value),
                price_0_001_g_ml   =float(price_0_001_g_ml),
                price_0_01_g_ml    =float(price_0_01_g_ml),
                price_0_1_g_ml     =float(price_0_1_g_ml),
                price_1_g_ml       =float(price_1_g_ml),
                price_10_g_ml      =float(price_10_g_ml),
                price_100_g_ml     =float(price_100_g_ml),
                price_500_g_ml     =float(price_500_g_ml),
                price_1000_g_ml    =float(price_1000_g_ml),
                )
            model.save()
