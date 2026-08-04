import pandas as pd
import numpy as np
import os

def limpiar_y_transformar():
    # 1. Cargar datos crudos
    ruta_raw = 'data/raw/datos_ecuador_bce.csv'
    df = pd.read_csv(ruta_raw)
    
    # Asegurar formato de fecha e índice temporal
    df['fecha'] = pd.to_datetime(df['fecha'])
    df.set_index('fecha', inplace=True)
    
    # 2. Transformaciones econométricas
    # Logaritmos para estabilizar la varianza
    df['log_pib'] = np.log(df['pib'])
    df['log_petroleo'] = np.log(df['petroleo'])
    df['log_riesgo'] = np.log(df['riesgo'])
    
    # Primeras diferencias para lograr estacionariedad
    df['d_log_pib'] = df['log_pib'].diff()
    df['d_log_petroleo'] = df['log_petroleo'].diff()
    df['d_log_riesgo'] = df['log_riesgo'].diff()
    
    # Eliminar el primer valor nulo generado por el diff()
    df_clean = df.dropna()
    
    # 3. Guardar en data/processed/
    os.makedirs('data/processed', exist_ok=True)
    ruta_processed = 'data/processed/datos_modelo_var.csv'
    df_clean.to_csv(ruta_processed)
    
    print(f"✅ Datos limpios y transformados guardados en: {ruta_processed}")

if __name__ == '__main__':
    limpiar_y_transformar()