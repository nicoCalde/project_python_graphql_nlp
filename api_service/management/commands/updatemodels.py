from django.core.management.base import BaseCommand
import pandas as pd
from api_service.models import Cars

class Command(BaseCommand):
    help = 'Import car data from CSV file'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            # Leer el archivo CSV sin manipular valores nulos
            df = pd.read_csv('cars.csv', delimiter=',')
        except Exception as e:
            self.stderr.write(f"Error reading the CSV file: {e}")
            return

        for index, row in df.iterrows():
            try:
                car = Cars(
                    make=row.get('Make', None),
                    model=row.get('Model', None),
                    year=row.get('Year', None),
                    engine_fuel_type=row.get('Engine Fuel Type', None),
                    engine_hp=row.get('Engine HP', None),
                    engine_cylinders=row.get('Engine Cylinders', None),
                    transmission_type=row.get('Transmission Type', None),
                    driven_wheels=row.get('Driven_Wheels', None),
                    number_of_doors=row.get('Number of Doors', None),
                    market_category=row.get('Market Category', None),
                    vehicle_size=row.get('Vehicle Size', None),
                    vehicle_style=row.get('Vehicle Style', None),
                    highway_mpg=row.get('highway MPG', None),
                    city_mpg=row.get('city mpg', None),
                    popularity=row.get('Popularity', None),
                    msrp=row.get('MSRP', None),
                )
                car.save()
            except Exception as e:
                self.stderr.write(f"Error saving row {index}: {e}")
