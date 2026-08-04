import pandas as pd
import json
import os

def generar_json_para_dashboard():
    # 1. Cargar datos procesados
    df = pd.read_csv('data/processed/datos_modelo_var.csv')
    
    # 2. Formatear datos para el dashboard/frontend
    historico = df[['fecha', 'pib', 'petroleo', 'riesgo']].to_dict(orient='records')
    
    # 3. Estructurar el JSON final
    resultados = {
        "titulo": "Modelo VAR: Crecimiento, Petróleo y Riesgo País en Ecuador",
        "cobertura": "2010 - 2024 (Frecuencia Trimestral)",
        "fuentes": "Banco Central del Ecuador (BCE) y FRED",
        "variables": ["PIB", "Precio del Petróleo (WTI)", "Riesgo País (EMBI)"],
        "modelo_estable": True,
        "historico": historico
    }
    
    # 4. Guardar en outputs/results/
    os.makedirs('outputs/results', exist_ok=True)
    ruta_json = 'outputs/results/datos_dashboard.json'
    
    with open(ruta_json, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)
        
    print(f"✅ Archivo JSON para el Dashboard guardado exitosamente en: {ruta_json}")

if __name__ == '__main__':
    generar_json_para_dashboard()