# 📡 Telco OFCS & Billing Engine (Motor de Tarifación Postpago)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-green.svg)
![Telco](https://img.shields.io/badge/Domain-Telecom%20%2F%20VAS-orange.svg)

## 📌 Descripción del Proyecto
Este proyecto es una simulación funcional de un **Offline Charging System (OFCS)**, el core financiero utilizado en las redes de telecomunicaciones móviles para el procesamiento, tasación (Rating) y facturación (Billing) del tráfico Postpago.

El sistema procesa registros de llamadas (CDRs - *Call Detail Records*) en bruto, cruza el consumo de red con un catálogo de reglas de negocio financieras y consolida la facturación mensual por usuario mediante procesos de extracción y transformación de datos (ETL).

## ⚙️ Arquitectura del Sistema

El proyecto está dividido en tres módulos secuenciales:

1. **Generador de Tráfico (Fase 1):** Simula el comportamiento de nodos de red (como MSC o PGW) generando miles de CDRs aleatorios de Voz, SMS y Datos asociados a identificadores IMSI.
2. **Motor de Tasación - Rating Engine (Fase 2):** Ingesta los CDRs crudos, clasifica el tipo de payload y aplica un modelo de costeo basado en tarifas predefinidas para convertirlos en EDRs (*Event Detail Records*).
3. **Módulo de Facturación - Billing (Fase 3):** Utiliza **Pandas** para agrupar los millones de eventos tasados y emitir un reporte consolidado de facturación mensual por cliente.

## 🚀 Instrucciones de Ejecución

Para correr la simulación del ciclo de facturación completo, ejecuta los scripts en el siguiente orden:

```bash
# 1. Generar la materia prima (CDRs)
python OFCS_GENERATOR.py

# 2. Ejecutar el motor de valoración financiera
python OFCS_RATING.py

# 3. Consolidar el recibo de facturación mensual
python OFCS_BILLING.py
