from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema
from .views import CarsList, CarsDetail
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Define your Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="API Suite",
        default_version='v0.0.1',
        description="This API allows users to manage car data including makes, models, and years. It provides endpoints for creating, retrieving, updating, and deleting car entries.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="31723375@ifts24.edu.ar, 30467866@ifts24.edu.ar"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('api/cars/', CarsList.as_view(), name='cars-list'),
    path('api/cars/<int:pk>/', CarsDetail.as_view(), name='cars-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='swagger-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-schema'),
]