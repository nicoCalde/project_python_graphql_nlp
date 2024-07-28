from django.core.management.base import BaseCommand
import pandas as pd
from api_service.models import ECommerceAnalytics

class Command(BaseCommand):
    help = 'Import e-commerce analytics data from CSV file'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Database connections here
        try:
            # Read the CSV file with the correct delimiter
            df = pd.read_csv('Data example - Python Coding Challenge - GraphQL.csv', delimiter=',')

            # Fill missing values in any string fields if necessary and convert them to strings
            string_columns = [
                'desc_ga_sku_producto', 'SASASA', 'desc_ga_nombre_producto_1', 'desc_ga_sku_producto_1', 
                'desc_ga_marca_producto', 'desc_categoria_producto', 'desc_categoria_prod_principal'
            ]
            for col in string_columns:
                df[col] = df[col].fillna('').astype(str)

        except Exception as e:
            self.stderr.write(f"Error reading the CSV file: {e}")
            return

        for index, row in df.iterrows():
            try:
                # Validate and clean the data as needed
                id_tie_fecha_valor = row['id_tie_fecha_valor']
                id_cli_cliente = row['id_cli_cliente']
                id_ga_vista = row['id_ga_vista']
                id_ga_tipo_dispositivo = row['id_ga_tipo_dispositivo']
                id_ga_fuente_medio = row['id_ga_fuente_medio']
                desc_ga_sku_producto = row['desc_ga_sku_producto']
                desc_ga_categoria_producto = row['desc_ga_categoria_producto']
                fc_agregado_carrito_cant = row['fc_agregado_carrito_cant']
                fc_ingreso_producto_monto = row['fc_ingreso_producto_monto']
                fc_retirado_carrito_cant = row['fc_retirado_carrito_cant']
                fc_detalle_producto_cant = row['fc_detalle_producto_cant']
                fc_producto_cant = row['fc_producto_cant']
                desc_ga_nombre_producto = row['desc_ga_nombre_producto']
                fc_visualizaciones_pag_cant = row['fc_visualizaciones_pag_cant']
                flag_pipol = row['flag_pipol']
                SASASA = row['SASASA']
                id_ga_producto = row['id_ga_producto']
                desc_ga_nombre_producto_1 = row['desc_ga_nombre_producto_1']
                desc_ga_sku_producto_1 = row['desc_ga_sku_producto_1']
                desc_ga_marca_producto = row['desc_ga_marca_producto']
                desc_ga_cod_producto = row['desc_ga_cod_producto']
                desc_categoria_producto = row['desc_categoria_producto']
                desc_categoria_prod_principal = row['desc_categoria_prod_principal']

                # Create and save the model instance
                ecommerce_analytics = ECommerceAnalytics(
                    id_tie_fecha_valor=id_tie_fecha_valor,
                    id_cli_cliente=id_cli_cliente,
                    id_ga_vista=id_ga_vista,
                    id_ga_tipo_dispositivo=id_ga_tipo_dispositivo,
                    id_ga_fuente_medio=id_ga_fuente_medio,
                    desc_ga_sku_producto=desc_ga_sku_producto,
                    desc_ga_categoria_producto=desc_ga_categoria_producto,
                    fc_agregado_carrito_cant=fc_agregado_carrito_cant,
                    fc_ingreso_producto_monto=fc_ingreso_producto_monto,
                    fc_retirado_carrito_cant=fc_retirado_carrito_cant,
                    fc_detalle_producto_cant=fc_detalle_producto_cant,
                    fc_producto_cant=fc_producto_cant,
                    desc_ga_nombre_producto=desc_ga_nombre_producto,
                    fc_visualizaciones_pag_cant=fc_visualizaciones_pag_cant,
                    flag_pipol=flag_pipol,
                    SASASA=SASASA,
                    id_ga_producto=id_ga_producto,
                    desc_ga_nombre_producto_1=desc_ga_nombre_producto_1,
                    desc_ga_sku_producto_1=desc_ga_sku_producto_1,
                    desc_ga_marca_producto=desc_ga_marca_producto,
                    desc_ga_cod_producto=desc_ga_cod_producto,
                    desc_categoria_producto=desc_categoria_producto,
                    desc_categoria_prod_principal=desc_categoria_prod_principal
                )
                ecommerce_analytics.save()
            except Exception as e:
                self.stderr.write(f"Error saving row {index}: {e}")