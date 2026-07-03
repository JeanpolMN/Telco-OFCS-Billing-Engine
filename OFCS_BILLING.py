import pandas as pd
import os

# =========================================================
# 1. CONTROL DE DIRECTORIO ABSOLUTO
# =========================================================
try:
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
except NameError:
    directorio_actual = os.getcwd()

ARCHIVO_ENTRADA = os.path.join(directorio_actual, 'cdrs_tasados.csv')
ARCHIVO_SALIDA = os.path.join(directorio_actual, 'facturacion_mensual.csv')

def ejecutar_facturacion():
    print("Iniciando Módulo de Facturación (Billing)...")
    
    if not os.path.exists(ARCHIVO_ENTRADA):
        print(f"ERROR: No se encontró el archivo tasado en:\n---> {ARCHIVO_ENTRADA}")
        return

    try:
        # 2. Cargar los datos tasados (ETL)
        df = pd.read_csv(ARCHIVO_ENTRADA)
        
        # 3. Agrupación matemática (Consolidación)
        # Sumamos el costo total por cada IMSI
        df_costo = df.groupby('IMSI')['Costo_Total_PEN'].sum().reset_index()
        
        # Pivotamos la tabla para sumar los volúmenes por cada tipo de servicio
        df_volumen = df.pivot_table(index='IMSI', columns='Tipo_Servicio', values='Volumen', aggfunc='sum', fill_value=0).reset_index()
        
        # 4. Unir y estructurar la factura final
        df_factura = pd.merge(df_volumen, df_costo, on='IMSI')
        
        # Renombramos las columnas para el reporte de negocio
        df_factura.rename(columns={
            'DATA': 'Datos_Consumidos_MB',
            'SMS': 'SMS_Enviados',
            'VOICE': 'Voz_Consumida_Segundos',
            'Costo_Total_PEN': 'Total_a_Pagar_PEN'
        }, inplace=True)
        
        # Redondeamos el total a 2 decimales (estándar financiero)
        df_factura['Total_a_Pagar_PEN'] = df_factura['Total_a_Pagar_PEN'].round(2)
        
        # 5. Exportar el recibo final consolidado
        df_factura.to_csv(ARCHIVO_SALIDA, index=False)
        
        print("¡Éxito! El ciclo de facturación mensual se ha completado.")
        print("Tu reporte consolidado (Invoice) se guardó en:")
        print(f"---> {ARCHIVO_SALIDA}")
        
    except Exception as e:
        print(f"Error inesperado procesando los datos con Pandas: {e}")

if __name__ == "__main__":
    ejecutar_facturacion()