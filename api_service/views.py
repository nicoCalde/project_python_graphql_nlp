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

'''
    FEATURE SPECIFICATION OF THE NLP ENDPOINT
    For a more advanced dialogue system between the user and the database, 
    an API should be implemented to:
        - Interpret user queries,
        - Analyze database responses, 
        - Perform the necessary analysis.
'''

def generate_natural_language_response(query, results):
    total_results = len(results)
    if total_results == 0:
        return f"Sorry, I couldn't find any data matching your query: '{query}'."
    
    response = f"Based on your query: '{query}', I found {total_results} result(s). Here are the details:\n"
    
    # Limit the number of items in the response
    max_items = 5
    items_to_display = results[:max_items]
    
    for idx, row in enumerate(items_to_display):
        row_str = ', '.join(f"{k}: {v}" for k, v in row.items())
        response += f"{idx + 1}. {row_str}\n"
    
    if total_results > max_items:
        response += f"\nThere are more results available. Only the first {max_items} items are displayed."

    return response

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
                        'response': openapi.Schema(type=openapi.TYPE_STRING, description='Natural language response'),
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

        # Use spaCy to process the query
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
        response_data = serializer.data

        # Generate natural language response
        natural_language_response = generate_natural_language_response(query, response_data)

        return Response({'response': natural_language_response})

class ECommerceAnalyticsListCreate(generics.ListCreateAPIView):
    queryset = ECommerceAnalytics.objects.all()
    serializer_class = ECommerceAnalyticsSerializer

class ECommerceAnalyticsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ECommerceAnalytics.objects.all()
    serializer_class = ECommerceAnalyticsSerializer