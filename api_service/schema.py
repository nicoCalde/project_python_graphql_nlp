import graphene
from graphene_django.types import DjangoObjectType
from .models import Cars

class CarsType(DjangoObjectType):
    class Meta:
        model = Cars

class Query(graphene.ObjectType):
    all_cars = graphene.List(
        CarsType,
        id=graphene.Int(),
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
        filters = {}
        for key, value in kwargs.items():
            if value is not None:
                if key == "make":
                    filters["make__iexact"] = value  # Insensible a mayúsculas
                elif key == "model":
                    filters["model__icontains"] = value  # Contiene en cualquier parte
                elif key == "year":
                    filters["year"] = value  # Año exacto
                elif key == "msrp":
                    filters["msrp__lte"] = value  # Menor o igual que el valor dado
                else:
                    filters[key] = value  # Filtro directo para otros campos
        return Cars.objects.filter(**filters)

schema = graphene.Schema(query=Query)