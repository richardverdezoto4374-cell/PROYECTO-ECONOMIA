import pandas as pd
import numpy as np
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller, grangercausalitytests
import matplotlib.pyplot as plt
import os

def estimar_modelo_var():
    # 1. Cargar los datos limpios
    ruta_processed = 'data/processed/datos_modelo_var.csv'
    df = pd.read_csv(ruta_processed, index_col=0, parse_dates=True)
    
    # Seleccionar las variables transformadas (primeras diferencias logarítmicas)
    var_data = df[['d_log_pib', 'd_log_petroleo', 'd_log_riesgo']].dropna()
    
    print("==================================================")
    print(" 1. PRUEBA DE ESTACIONARIEDAD (Dickey-Fuller)")
    print("==================================================")
    for col in var_data.columns:
        res = adfuller(var_data[col])
        print(f"Variable {col}: p-valor = {res[1]:.4f}")
        if res[1] < 0.05:
            print(f"  -> {col} es ESTACIONARIA (p < 0.05)")
        else:
            print(f"  -> {col} NO es estacionaria")
            
    print("\n==================================================")
    print(" 2. SELECCIÓN DE REZAGOS ÓPTIMOS")
    print("==================================================")
    model = VAR(var_data)
    lag_order = model.select_order(maxlags=4)
    print(lag_order.summary())
    
    # Usar el rezago recomendado por AIC
    opt_lag = lag_order.aic
    print(f"\nRezagos seleccionados según AIC: {opt_lag}")
    
    # 3. Estimación del Modelo VAR
    results = model.fit(opt_lag)
    print("\n==================================================")
    print(" 3. RESUMEN DEL MODELO VAR ESTIMADO")
    print("==================================================")
    print(results.summary())
    
    # 4. Pruebas de Diagnóstico
    print("\n==================================================")
    print(" 4. DIAGNÓSTICO DE RESIDUOS Y ESTABILIDAD")
    print("==================================================")
    is_stable = results.is_stable()
    print(f"¿El modelo VAR es estable?: {is_stable}")
    
    # 5. Generar y Guardar Funciones Impulso-Respuesta (FIR)
    os.makedirs('outputs/figures', exist_ok=True)
    irf = results.irf(10)
    fig_irf = irf.plot(orth=True) # <-- AQUÍ SE CORRIGIÓ 'orth=True'
    fig_irf.suptitle("Funciones Impulso-Respuesta (FIR)", fontsize=14)
    plt.tight_layout()
    ruta_fig = 'outputs/figures/impulso_respuesta.png'
    plt.savefig(ruta_fig)
    plt.close()
    print(f"\n✅ Gráfico de Impulso-Respuesta guardado en: {ruta_fig}")
    
    # 6. Guardar resumen del modelo a texto en outputs/tables/
    os.makedirs('outputs/tables', exist_ok=True)
    with open('outputs/tables/resumen_modelo_var.txt', 'w', encoding='utf-8') as f:
        f.write(str(results.summary()))
    print("✅ Tabla con resumen del modelo guardada en: outputs/tables/resumen_modelo_var.txt")

if __name__ == '__main__':
    estimar_modelo_var()