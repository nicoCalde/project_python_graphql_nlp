import graphene
from graphene_django.types import DjangoObjectType
from .models import Cars

class CarsType(DjangoObjectType):
    class Meta:
        model = Cars

class Query(graphene.ObjectType):
    all_cars = graphene.List(
        CarsType,
        make=graphene.String(),
        model=graphene.String(),
        year=graphene.Int(),
        engine_fuel_type=graphene.String(),
        engine_hp=graphene.Float(),
        engine_cylinders=graphene.Float(),
        transmission_type=graphene.String(),
        driven_wheels=graphene.String(),
        number_of_doors=graphene.Float(),
        market_category=graphene.String(),
        vehicle_size=graphene.String(),
        vehicle_style=graphene.String(),
        highway_mpg=graphene.Int(),
        city_mpg=graphene.Int(),
        popularity=graphene.Int(),
        msrp=graphene.Int(),
    )

    def resolve_all_cars(self, info, **kwargs):
        filters = {k: v for k, v in kwargs.items() if v is not None}
        return Cars.objects.filter(**filters)

schema = graphene.Schema(query=Query)