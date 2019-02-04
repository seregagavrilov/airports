from django.core.management.base import BaseCommand
from django.apps import apps
import pandas as pd


class Command(BaseCommand):
    help = 'Initial data loading into the system'

    def handle(self, *args, **kwargs):
        file_path = kwargs['path']
        Airport = apps.get_model('rest_api_airports', 'Airport')
        City = apps.get_model('rest_api_airports', 'City')
        Country = apps.get_model('rest_api_airports', 'Country')
        data = pd.read_csv(file_path, sep='|', encoding='cp1251')
        self.stdout.write( self.style.NOTICE('loading is started...'))
        for row in data.iterrows():
            row = row[1].drop_duplicates()
            try:
                iso_code = row[7]
            except IndexError:
                continue

            try:
                phone_number = row[9]
            except IndexError:
                phone_number = ''

            try:
                airstrip_length = row[8]
                airstrip_length = int(airstrip_length)
            except (IndexError, ValueError):
                airstrip_length = 0

            country = Country.objects.create(
                rus_name=row[5],
                eng_name=row[6],
                iso_code=iso_code
            )

            city = City.objects.create(
                rus_name=row[3],
                eng_name=row[4],
                country=country
            )
            Airport.objects.create(
                rus_name=row[1],
                eng_name=row[2],
                icao=row[0],
                phone_number=phone_number,
                city=city,
                airstrip_length=airstrip_length,
            )
        self.stdout.write(self.style.SUCCESS('loading is completed!'))

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='path to your file')


