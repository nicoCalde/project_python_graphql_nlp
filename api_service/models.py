from django.db import models

# Create your models here.

# Model representing e-commerce analytics data.
class ECommerceAnalytics(models.Model):
    id_tie_fecha_valor = models.IntegerField()
    id_cli_cliente = models.IntegerField()
    id_ga_vista = models.IntegerField()
    id_ga_tipo_dispositivo = models.IntegerField()
    id_ga_fuente_medio = models.IntegerField()
    desc_ga_sku_producto = models.CharField(max_length=255, null=True, blank=True)
    desc_ga_categoria_producto = models.FloatField(null=True, blank=True)
    fc_agregado_carrito_cant = models.IntegerField(null=True, blank=True)
    fc_ingreso_producto_monto = models.FloatField(null=True, blank=True)
    fc_retirado_carrito_cant = models.FloatField(null=True, blank=True)
    fc_detalle_producto_cant = models.IntegerField(null=True, blank=True)
    fc_producto_cant = models.IntegerField(null=True, blank=True)
    desc_ga_nombre_producto = models.FloatField(null=True, blank=True)
    fc_visualizaciones_pag_cant = models.FloatField(null=True, blank=True)
    flag_pipol = models.IntegerField(null=True, blank=True)
    SASASA = models.CharField(max_length=255, null=True, blank=True)
    id_ga_producto = models.IntegerField(null=True, blank=True)
    desc_ga_nombre_producto_1 = models.CharField(max_length=255, null=True, blank=True)
    desc_ga_sku_producto_1 = models.CharField(max_length=255, null=True, blank=True)
    desc_ga_marca_producto = models.CharField(max_length=255, null=True, blank=True)
    desc_ga_cod_producto = models.FloatField(null=True, blank=True)
    desc_categoria_producto = models.CharField(max_length=255, null=True, blank=True)
    desc_categoria_prod_principal = models.CharField(max_length=255, null=True, blank=True)
    # Reflects the structure and content of the provided CSV file, capturing all columns and their respective data types.

    def __str__(self):
        return f"Customer {self.id_cli_cliente} - Product {self.desc_ga_sku_producto}"
    # This __str__ method includes the customer ID and product SKU, providing a clear and concise representation of each record.