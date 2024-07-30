import graphene
from graphene_django import DjangoObjectType
from .models import ECommerceAnalytics

'''
Comments explaining the Query code:
 - The ECommerceAnalyticsType class is a DjangoObjectType that maps the ECommerceAnalytics model fields to GraphQL fields.
 - The Query class defines GraphQL queries for fetching all ECommerceAnalytics records and fetching records based on various id fields and SKU.
 - The resolve_all_analytics method returns all records in the ECommerceAnalytics model.
 - Each resolve_analytics_by_* method returns records matching the provided field value.
 - The schema is defined with the Query class, allowing the defined queries to be used in the GraphQL endpoint.

Note: You can add more queries as needed based on other fields in the model. Each query can help fetch specific data that might be required by the application or analysis.
'''

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

# Define a query for fetching all ECommerceAnalytics records (just access to the data as requested)
class Query(graphene.ObjectType):
    all_analytics = graphene.List(ECommerceAnalyticsType)

    def resolve_all_analytics(root, info):
        # Return all records from the ECommerceAnalytics model
        return ECommerceAnalytics.objects.all()
    
    # Define all aditional queries needed

    # Define queries for fetching ECommerceAnalytics records by various id fields and SKU
    analytics_by_id_tie_fecha_valor = graphene.List(ECommerceAnalyticsType, id_tie_fecha_valor=graphene.Int(required=True))

    def resolve_analytics_by_id_tie_fecha_valor(root, info, id_tie_fecha_valor):
        # Return records matching the provided id_tie_fecha_valor
        return ECommerceAnalytics.objects.filter(id_tie_fecha_valor=id_tie_fecha_valor)

    analytics_by_id_cli_cliente = graphene.List(ECommerceAnalyticsType, id_cli_cliente=graphene.Int(required=True))

    def resolve_analytics_by_id_cli_cliente(root, info, id_cli_cliente):
        # Return records matching the provided id_cli_cliente
        return ECommerceAnalytics.objects.filter(id_cli_cliente=id_cli_cliente)

    analytics_by_id_ga_vista = graphene.List(ECommerceAnalyticsType, id_ga_vista=graphene.Int(required=True))

    def resolve_analytics_by_id_ga_vista(root, info, id_ga_vista):
        # Return records matching the provided id_ga_vista
        return ECommerceAnalytics.objects.filter(id_ga_vista=id_ga_vista)

    analytics_by_id_ga_tipo_dispositivo = graphene.List(ECommerceAnalyticsType, id_ga_tipo_dispositivo=graphene.Int(required=True))

    def resolve_analytics_by_id_ga_tipo_dispositivo(root, info, id_ga_tipo_dispositivo):
        # Return records matching the provided id_ga_tipo_dispositivo
        return ECommerceAnalytics.objects.filter(id_ga_tipo_dispositivo=id_ga_tipo_dispositivo)

    analytics_by_id_ga_fuente_medio = graphene.List(ECommerceAnalyticsType, id_ga_fuente_medio=graphene.Int(required=True))

    def resolve_analytics_by_id_ga_fuente_medio(root, info, id_ga_fuente_medio):
        # Return records matching the provided id_ga_fuente_medio
        return ECommerceAnalytics.objects.filter(id_ga_fuente_medio=id_ga_fuente_medio)

    analytics_by_id_ga_producto = graphene.List(ECommerceAnalyticsType, id_ga_producto=graphene.Int(required=True))

    def resolve_analytics_by_id_ga_producto(root, info, id_ga_producto):
        # Return records matching the provided id_ga_producto
        return ECommerceAnalytics.objects.filter(id_ga_producto=id_ga_producto)

    analytics_by_sku = graphene.List(ECommerceAnalyticsType, desc_ga_sku_producto=graphene.String(required=True))

    def resolve_analytics_by_sku(root, info, desc_ga_sku_producto):
        # Return records matching the provided desc_ga_sku_producto
        return ECommerceAnalytics.objects.filter(desc_ga_sku_producto=desc_ga_sku_producto)

schema = graphene.Schema(query=Query)