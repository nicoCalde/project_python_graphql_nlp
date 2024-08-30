from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from .models import Cars
from .serializers import CarsSerializer

# Create your views here.
class CarsList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

class CarsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer