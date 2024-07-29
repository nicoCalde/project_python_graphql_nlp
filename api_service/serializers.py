from rest_framework import serializers
from .models import ECommerceAnalytics

class ECommerceAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECommerceAnalytics
        fields = '__all__'  # Include all fields from the model