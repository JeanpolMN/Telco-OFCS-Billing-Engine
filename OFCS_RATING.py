import csv

# Catálogo de Precios (Simulando tarifas comerciales en Soles - PEN)
TARIFAS = {
    'VOICE': 0.01,  # S/ 0.01 por segundo hablado
    'SMS': 0.10,    # S/ 0.10 por cada mensaje enviado
    'DATA': 0.05    # S/ 0.05 por cada Megabyte consumido
}

ARCHIVO_ENTRADA = 'cdrs_generados.csv'
ARCHIVO_SALIDA = 'cdrs_tasados.csv'

def tasar_evento(servicio, volumen):
    """
    Motor matemático que aplica la regla de negocio.
    Multiplica el volumen consumido por el precio unitario del servicio.
    """
    precio_unitario = TARIFAS.get(servicio, 0.0)
    costo_total = float(volumen) * precio_unitario
    # Redondeamos a 4 decimales como se hace en los sistemas financieros Telco
    return round(costo_total, 4) 

def ejecutar_rating():
    print("Iniciando Motor de Tasación (Rating Engine)...")
    registros_tasados = []
    
    try:
        # 1. Lectura del archivo crudo
        with open(ARCHIVO_ENTRADA, mode='r', encoding='utf-8') as archivo_in:
            lector = csv.reader(archivo_in)
            cabeceras = next(lector)
            
            # Agregamos la nueva columna financiera a las cabeceras
            cabeceras.append('Costo_Total_PEN')
            registros_tasados.append(cabeceras)
            
            # 2. Procesamiento línea por línea (Parsing y Rating)
            contador = 0
            for fila in lector:
                servicio = fila[1]
                volumen = fila[3]
                
                # Invocamos la función de tasación
                costo = tasar_evento(servicio, volumen)
                
                # Adjuntamos el costo calculado al final de la fila
                fila.append(costo)
                registros_tasados.append(fila)
                contador += 1
                
        # 3. Escritura del nuevo archivo tasado
        with open(ARCHIVO_SALIDA, mode='w', newline='', encoding='utf-8') as archivo_out:
            escritor = csv.writer(archivo_out)
            escritor.writerows(registros_tasados)
            
        print(f"¡Operación exitosa! Se procesaron y tasaron {contador} CDRs.")
        print(f"Archivo generado exitosamente: '{ARCHIVO_SALIDA}'.")
        
    except FileNotFoundError:
        print(f"\n❌ ERROR CRÍTICO:")
        print(f"No se encontró el archivo '{ARCHIVO_ENTRADA}' en este directorio.")
        print("POR FAVOR: Asegúrate de ejecutar primero tu script de la Fase 1 para crear los datos.")

if __name__ == "__main__":
    ejecutar_rating()