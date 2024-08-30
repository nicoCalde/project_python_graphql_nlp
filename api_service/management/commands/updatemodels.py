from django.core.management.base import BaseCommand
import pandas as pd
from api_service.models import Cars

class Command(BaseCommand):
    help = 'Import car data from CSV file'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Database connections here
        try:
            # Read the CSV file with the correct delimiter
            df = pd.read_csv('cars.csv', delimiter=',')

            # Fill missing values in any string fields if necessary and convert them to strings
            # In this case, we ensure all fields can accept nulls or be blank, so no need for extensive filling
            df = df.fillna(None)

        except Exception as e:
            self.stderr.write(f"Error reading the CSV file: {e}")
            return

        for index, row in df.iterrows():
            try:
                # Validate and clean the data as needed
                make = row['Make']
                model = row['Model']
                year = row['Year']
                engine_fuel_type = row['Engine Fuel Type']
                engine_hp = row['Engine HP']
                engine_cylinders = row['Engine Cylinders']
                transmission_type = row['Transmission Type']
                driven_wheels = row['Driven_Wheels']
                number_of_doors = row['Number of Doors']
                market_category = row['Market Category']
                vehicle_size = row['Vehicle Size']
                vehicle_style = row['Vehicle Style']
                highway_mpg = row['highway MPG']
                city_mpg = row['city mpg']
                popularity = row['Popularity']
                msrp = row['MSRP']

                # Create and save the model instance
                car = Cars(
                    make=make,
                    model=model,
                    year=year,
                    engine_fuel_type=engine_fuel_type,
                    engine_hp=engine_hp,
                    engine_cylinders=engine_cylinders,
                    transmission_type=transmission_type,
                    driven_wheels=driven_wheels,
                    number_of_doors=number_of_doors,
                    market_category=market_category,
                    vehicle_size=vehicle_size,
                    vehicle_style=vehicle_style,
                    highway_mpg=highway_mpg,
                    city_mpg=city_mpg,
                    popularity=popularity,
                    msrp=msrp
                )
                car.save()
            except Exception as e:
                self.stderr.write(f"Error saving row {index}: {e}")