from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
import spacy
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from .models import ECommerceAnalytics
from .serializers import ECommerceAnalyticsSerializer

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Create your views here.
class nlp_endpoint(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'query': openapi.Schema(type=openapi.TYPE_STRING, description='The search query'),
            },
            required=['query']
        ),
        responses={
            200: openapi.Response(
                description='Successful response',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'total_results': openapi.Schema(type=openapi.TYPE_INTEGER, description='Total number of results'),
                        'results': openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    'id_tie_fecha_valor': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'id_cli_cliente': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'id_ga_vista': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'id_ga_tipo_dispositivo': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'id_ga_fuente_medio': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'desc_ga_sku_producto': openapi.Schema(type=openapi.TYPE_STRING),
                                    'desc_ga_categoria_producto': openapi.Schema(type=openapi.TYPE_NUMBER),
                                    'fc_agregado_carrito_cant': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'fc_ingreso_producto_monto': openapi.Schema(type=openapi.TYPE_NUMBER),
                                    'fc_retirado_carrito_cant': openapi.Schema(type=openapi.TYPE_NUMBER),
                                    'fc_detalle_producto_cant': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'fc_producto_cant': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'desc_ga_nombre_producto': openapi.Schema(type=openapi.TYPE_NUMBER),
                                    'fc_visualizaciones_pag_cant': openapi.Schema(type=openapi.TYPE_NUMBER),
                                    'flag_pipol': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'SASASA': openapi.Schema(type=openapi.TYPE_STRING),
                                    'id_ga_producto': openapi.Schema(type=openapi.TYPE_INTEGER),
                                    'desc_ga_nombre_producto_1': openapi.Schema(type=openapi.TYPE_STRING),
                                    'desc_ga_sku_producto_1': openapi.Schema(type=openapi.TYPE_STRING),
                                    'desc_ga_marca_producto': openapi.Schema(type=openapi.TYPE_STRING),
                                    'desc_ga_cod_producto': openapi.Schema(type=openapi.TYPE_NUMBER),
                                    'desc_categoria_producto': openapi.Schema(type=openapi.TYPE_STRING),
                                    'desc_categoria_prod_principal': openapi.Schema(type=openapi.TYPE_STRING),
                                }
                            )
                        ),
                    }
                )
            ),
            400: openapi.Response(
                description='Bad request',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        query = request.data.get('query', '')

        if not query:
            return Response({'error': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Normalize the query to lowercase
        query = query.lower()

        # General search across all fields
        doc = nlp(query)
        keywords = [ent.text.lower() for ent in doc.ents]

        # If no entities are recognized, use the entire query as a keyword
        if not keywords:
            keywords = query.lower().split()

        # Build the query to search across all fields
        query_filter = Q()
        for field in ECommerceAnalytics._meta.get_fields():
            if field.get_internal_type() in ['CharField', 'TextField']:
                field_name = field.name
                for keyword in keywords:
                    query_filter |= Q(**{f"{field_name}__icontains": keyword})

        # Query the database
        matching_rows = ECommerceAnalytics.objects.filter(query_filter)

        # Serialize the results
        serializer = ECommerceAnalyticsSerializer(matching_rows, many=True)
        response_data = {
            'total_results': len(serializer.data),
            'results': serializer.data
        }

        return Response(response_data)

class ECommerceAnalyticsListCreate(generics.ListCreateAPIView):
    queryset = ECommerceAnalytics.objects.all()
    serializer_class = ECommerceAnalyticsSerializer

class ECommerceAnalyticsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ECommerceAnalytics.objects.all()
    serializer_class = ECommerceAnalyticsSerializer