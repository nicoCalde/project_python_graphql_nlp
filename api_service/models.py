from django.db import models

# Create your models here.
class Cars(models.Model):
    make = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    engine_fuel_type = models.CharField(max_length=100, null=True, blank=True)
    engine_hp = models.FloatField(null=True, blank=True)
    engine_cylinders = models.FloatField(null=True, blank=True)
    transmission_type = models.CharField(max_length=100, null=True, blank=True)
    driven_wheels = models.CharField(max_length=100, null=True, blank=True)
    number_of_doors = models.FloatField(null=True, blank=True)
    market_category = models.CharField(max_length=100, null=True, blank=True)
    vehicle_size = models.CharField(max_length=100, null=True, blank=True)
    vehicle_style = models.CharField(max_length=100, null=True, blank=True)
    highway_mpg = models.IntegerField(null=True, blank=True)
    city_mpg = models.IntegerField(null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    msrp = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.make} - {self.model} - {self.year}"