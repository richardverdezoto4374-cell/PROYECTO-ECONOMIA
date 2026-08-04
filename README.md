# Impacto del Precio del Petróleo y el Riesgo País sobre el Crecimiento Económico en Ecuador: Un Enfoque VAR (2010–2024)

## Resumen del Proyecto

Este repositorio alberga la implementación econométrica completa para analizar la transmisión de perturbaciones macroeconómicas externas —específicamente variaciones en el precio internacional del petróleo WTI y fluctuaciones en el índice de riesgo país (EMBI)— sobre la tasa de crecimiento del Producto Interno Bruto (PIB) real de Ecuador durante el periodo 2010-2024.

---

## 1. Formulación del Problema y Objetivos

* **Pregunta de Investigación:** ¿De qué manera y en qué magnitud inciden los shocks exógenos en el precio del petróleo WTI y las fluctuaciones del riesgo país (EMBI) sobre la tasa de crecimiento del Producto Interno Bruto (PIB) real en el Ecuador durante el periodo 2010–2024?
* **Objetivo General:** Analizar cuantitativamente la dinámica de transmisión de shocks externos hacia el crecimiento económico del Ecuador mediante la estimación de un modelo econométrico multivariado Vector Autorregresivo (VAR).
* **Hipótesis:** Las perturbaciones positivas en los precios del petróleo ejercen un estímulo transitorio sobre el nivel de actividad económica en el corto plazo, mientras que incrementos en el riesgo país generan efectos contractivos de mayor persistencia debido al encarecimiento del financiamiento.

---

## 2. Fuentes de Datos y Variables

1. **Producto Interno Bruto (PIB Real):** Banco Central del Ecuador (BCE).
2. **Precio del Petróleo WTI (USD/barril):** Federal Reserve Bank of St. Louis (FRED) / Banco Central del Ecuador.
3. **Riesgo País (Puntos básicos EMBI):** JP Morgan / Banco Central del Ecuador.

---

## 3. Estructura del Repositorio

```text
PROYECTO-ECONOMETRIA/
│
├── agents/             # Prompts y agentes de desarrollo
├── dashboard/          # Interfaz web (index.html) para despliegue en Vercel
├── data/               # Datos en formato bruto (raw) y procesado (processed)
├── notebooks/          # Cuadernos Jupyter para exploración gráfica y diagnósticos
├── outputs/            # Gráficos (figures), resultados (results) y tablas (tables)
├── paper/              # Minipaper académico en PDF
├── prompts/            # Registro de interacción y prompts de IA
├── src/                # Scripts de Python para procesamiento y modelado
├── .gitignore          # Archivos omitidos en Git
├── README.md           # Documentación principal del proyecto
└── requirements.txt    # Librerías y dependencias necesarias