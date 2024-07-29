from rest_framework import serializers
from .models import ECommerceAnalytics

class ECommerceAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECommerceAnalytics
        fields = '__all__'  # Include all fields from the model

# class ECommerceAnalyticsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ECommerceAnalytics
#         fields = '__all__'
#         extra_kwargs = {
#             'id_tie_fecha_valor': {'example': 20240130},
#             'id_cli_cliente': {'example': 123},
#             'id_ga_vista': {'example': 456},
#             # Add more examples for other fields
#         }