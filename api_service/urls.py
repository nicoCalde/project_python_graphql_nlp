from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema
from .views import ECommerceAnalyticsListCreate, ECommerceAnalyticsDetail, nlp_endpoint
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Define your Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v0.0.1',
        description="Description of the API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('nlp/', nlp_endpoint, name='nlp-endpoint'),
    path('api/ecommerce-analytics/', ECommerceAnalyticsListCreate.as_view(), name='ecommerce-analytics-list-create'),
    path('api/ecommerce-analytics/<int:pk>/', ECommerceAnalyticsDetail.as_view(), name='ecommerce-analytics-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='swagger-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-schema'),
]