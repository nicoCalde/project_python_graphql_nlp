import graphene
from graphene_django import DjangoObjectType
from .models import ECommerceAnalytics

# Define a GraphQL type for the ECommerceAnalytics model
class ECommerceAnalyticsType(DjangoObjectType):
    class Meta:
        model = ECommerceAnalytics
        # Fields to be included in the GraphQL type
        fields = (
            "id_tie_fecha_valor",
            "id_cli_cliente",
            "id_ga_vista",
            "id_ga_tipo_dispositivo",
            "id_ga_fuente_medio",
            "desc_ga_sku_producto",
            "desc_ga_categoria_producto",
            "fc_agregado_carrito_cant",
            "fc_ingreso_producto_monto",
            "fc_retirado_carrito_cant",
            "fc_detalle_producto_cant",
            "fc_producto_cant",
            "desc_ga_nombre_producto",
            "fc_visualizaciones_pag_cant",
            "flag_pipol",
            "SASASA",
            "id_ga_producto",
            "desc_ga_nombre_producto_1",
            "desc_ga_sku_producto_1",
            "desc_ga_marca_producto",
            "desc_ga_cod_producto",
            "desc_categoria_producto",
            "desc_categoria_prod_principal",
        )

# Define a query for fetching all ECommerceAnalytics records
class Query(graphene.ObjectType):
    all_analytics = graphene.List(ECommerceAnalyticsType)

    def resolve_all_analytics(root, info):
        # Return all records from the ECommerceAnalytics model
        return ECommerceAnalytics.objects.all()
    
    # Define aditional queries as needed

    # Define a query for fetching a single ECommerceAnalytics record by id_cli_cliente
    analytics_by_client = graphene.Field(ECommerceAnalyticsType, id_cli_cliente=graphene.Int(required=True))

    def resolve_analytics_by_client(root, info, id_cli_cliente):
        # Return a single record matching the provided id_cli_cliente
        try:
            return ECommerceAnalytics.objects.get(id_cli_cliente=id_cli_cliente)
        except ECommerceAnalytics.DoesNotExist:
            return None

    # Define a query for fetching ECommerceAnalytics records by device type
    analytics_by_device_type = graphene.List(ECommerceAnalyticsType, id_ga_tipo_dispositivo=graphene.Int(required=True))

    def resolve_analytics_by_device_type(root, info, id_ga_tipo_dispositivo):
        # Return records matching the provided id_ga_tipo_dispositivo
        return ECommerceAnalytics.objects.filter(id_ga_tipo_dispositivo=id_ga_tipo_dispositivo)

    # Define a query for fetching ECommerceAnalytics records by product SKU
    analytics_by_product_sku = graphene.List(ECommerceAnalyticsType, desc_ga_sku_producto=graphene.String(required=True))

    def resolve_analytics_by_product_sku(root, info, desc_ga_sku_producto):
        # Return records matching the provided desc_ga_sku_producto
        return ECommerceAnalytics.objects.filter(desc_ga_sku_producto=desc_ga_sku_producto)


schema = graphene.Schema(query=Query)

'''
Comments explaining the code:
 - The ECommerceAnalyticsType class is a DjangoObjectType that maps the ECommerceAnalytics model fields to GraphQL fields.
 - The Query class defines GraphQL queries for fetching all ECommerceAnalytics records and fetching a single record by id_cli_cliente or additional criteria.
 - The resolve_all_analytics method returns all records in the ECommerceAnalytics model.
 - The resolve_analytics_by_client method returns a single record based on the provided id_cli_cliente. If no record is found, it returns None.
 - The resolve_analytics_by_device_type method returns records matching the provided id_ga_tipo_dispositivo.
 - The resolve_analytics_by_product_sku method returns records matching the provided desc_ga_sku_producto.
 - The schema is defined with the Query class, allowing the defined queries to be used in the GraphQL endpoint.

Note: You can add more queries as needed based on other fields in the model. Each query can help fetch specific data that might be required by the application or analysis.
'''