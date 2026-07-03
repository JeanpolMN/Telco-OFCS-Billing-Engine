import csv
import random
from datetime import datetime, timedelta

# Configuración del simulador
NUM_REGISTROS = 5000
ARCHIVO_SALIDA = 'cdrs_generados.csv'

# Generamos 10 IMSIs simulados de Claro Perú (MCC: 716, MNC: 10)
imsis_clientes = [f"71610{str(random.randint(1000000000, 9999999999))}" for _ in range(10)]

# Tipos de servicios en la red
tipos_servicio = ['VOICE', 'SMS', 'DATA']

# Rango de fechas (Simulando el ciclo de facturación del último mes)
fecha_inicio = datetime.now() - timedelta(days=30)
fecha_fin = datetime.now()

def generar_fecha_aleatoria(inicio, fin):
    """Genera un timestamp aleatorio entre dos fechas."""
    diferencia = fin - inicio
    segundos_aleatorios = random.randrange(int(diferencia.total_seconds()))
    return inicio + timedelta(seconds=segundos_aleatorios)

def generar_cdrs():
    """Genera la lista de registros de llamadas (CDRs)."""
    cdrs = []
    for _ in range(NUM_REGISTROS):
        imsi = random.choice(imsis_clientes)
        servicio = random.choice(tipos_servicio)
        fecha_hora = generar_fecha_aleatoria(fecha_inicio, fecha_fin).strftime('%Y-%m-%d %H:%M:%S')
        
        # Lógica de volumen según el tipo de servicio
        if servicio == 'VOICE':
            # Llamadas entre 10 segundos y 15 minutos (900 seg)
            volumen = random.randint(10, 900) 
            unidad = 'Segundos'
        elif servicio == 'SMS':
            # Un SMS a la vez
            volumen = 1 
            unidad = 'Unidad'
        elif servicio == 'DATA':
            # Consumo de sesión de datos entre 1 MB y 500 MB
            volumen = round(random.uniform(1.0, 500.0), 2) 
            unidad = 'MB'
            
        cdrs.append([imsi, servicio, fecha_hora, volumen, unidad])
    
    # Ordenamos los registros cronológicamente para mayor realismo
    cdrs.sort(key=lambda x: datetime.strptime(x[2], '%Y-%m-%d %H:%M:%S'))
    return cdrs

# Ejecución y escritura del archivo CSV
if __name__ == "__main__":
    print("Iniciando la generación de CDRs de red...")
    datos_cdr = generar_cdrs()
    
    # Escribimos los datos en el archivo CSV
    with open(ARCHIVO_SALIDA, mode='w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        # Escribimos las cabeceras
        escritor.writerow(['IMSI', 'Tipo_Servicio', 'Fecha_Hora', 'Volumen', 'Unidad_Medida'])
        # Escribimos la data masiva
        escritor.writerows(datos_cdr)
        
    print(f"¡Éxito! Se generaron {NUM_REGISTROS} registros en el archivo '{ARCHIVO_SALIDA}'.")