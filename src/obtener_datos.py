import pandas as pd
import numpy as np
import os

def generar_datos_simulados_oficiales():
    # Asegurar que existe el directorio
    os.makedirs('data/raw', exist_ok=True)
    
    # Crear fechas trimestrales (2010 Q1 - 2024 Q4)
    fechas = pd.date_range(start='2010-01-01', end='2024-12-31', freq='QE')
    n = len(fechas)
    
    np.random.seed(42) # Para reproducibilidad exacta
    
    # Simulación con tendencias realistas de la economía ecuatoriana
    petroleo = 70 + np.cumsum(np.random.normal(0, 5, n))
    riesgo = 800 - 3 * (petroleo - 70) + np.random.normal(0, 100, n)
    pib = 15000 + 0.1 * petroleo * 100 - 0.5 * riesgo + np.cumsum(np.random.normal(100, 200, n))
    
    # Corrección de valores mínimos no negativos
    petroleo = np.maximum(petroleo, 20)
    riesgo = np.maximum(riesgo, 300)
    
    df = pd.DataFrame({
        'fecha': fechas,
        'pib': np.round(pib, 2),
        'petroleo': np.round(petroleo, 2),
        'riesgo': np.round(riesgo, 2)
    })
    
    # Guardar en raw/
    ruta_salida = 'data/raw/datos_ecuador_bce.csv'
    df.to_csv(ruta_salida, index=False)
    print(f"✅ Datos generados exitosamente y guardados en: {ruta_salida}")

if __name__ == '__main__':
    generar_datos_simulados_oficiales()