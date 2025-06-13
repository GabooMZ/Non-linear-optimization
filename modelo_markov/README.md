# 🔗 Modelo de Cadenas de Markov para Comportamiento de Pago

Esta carpeta contiene notebooks con el análisis del comportamiento de pago de los clientes usando **Modelos de Cadenas de Markov**. Se estudian transiciones entre distintos niveles de cumplimiento de pago mes a mes, para entender patrones de morosidad y segmentar a los clientes según su comportamiento.

Se realizó un análisis independiente por tipo de producto financiero:

- 📌 **Préstamo Personal (PP)**
- 🛍️ **Tarjeta de Crédito Departamental (TDC_Dept)**
- 💳 **Tarjeta de Crédito Visa (TDC_Visa)**

---

## 📁 Contenido de la Carpeta

- `analisis_markov_PP.ipynb`: Análisis de cadenas de Markov para Préstamos Personales.
- `analisis_markov_TDCdept.ipynb`: Análisis para Tarjetas Departamentales.
- `analisis_markov_TDCvisa.ipynb`: Análisis para Tarjetas Visa.

---

## 🎯 Objetivo

Modelar el **manejo de la deuda por parte del cliente** a través de un proceso estocástico que representa la probabilidad de moverse entre distintos estados de pago. Esto permite identificar patrones de transición (por ejemplo, de morosidad a pago puntual) y hacer una segmentación basada en comportamiento.

---

## 🔍 Estados Definidos

Se definieron **6 estados** para representar el cumplimiento de pago mensual de cada cliente:

| Estado | Descripción               |
|--------|---------------------------|
| 0      | No pagó                   |
| 1      | Pagó menos del mínimo     |
| 2      | Pagó el mínimo            |
| 3      | Pagó más del mínimo       |
| 4      | Pago completo             |
| 5      | Desactivado               |

---

## 🧠 Metodología

1. **Selección de variables**:  
   Se usaron las siguientes variables por mes:
   - `Pago_$M_i$`
   - `Pago_Mínimo_$M_i$`
   - `Saldo_total_$M_i$`

2. **Asignación de estados**:  
   Cada mes por cliente fue clasificado en uno de los 6 estados definidos. Aquellos clientes con solo un mes de historial fueron igualmente clasificados, pero no se usaron para calcular transiciones.

3. **Construcción de la matriz de transición**:  
   Por cada cliente con al menos 2 meses de historial, se contabilizaron las transiciones entre estados consecutivos para construir una **matriz de transición**.

4. **Análisis de propiedades de la matriz**:
   - Se discutieron las limitaciones por falta de **ergodicidad** (irreducibilidad, recurrencia positiva y aperiodicidad) debido al bajo número de observaciones por cliente (solo 6 meses).
   - Se sugieren dos caminos alternativos:
     - Reducir el espacio de estados.
     - Predecir el estado a un paso en vez de buscar convergencia.

5. **Clusterización determinista**:
   A partir del último estado observado por cliente y su matriz de transición, se identificó el siguiente estado con mayor probabilidad. Esto permitió realizar una **segmentación del portafolio** de clientes.

---

## 📊 Visualizaciones

Se generaron visualizaciones representativas de los clústeres obtenidos, tanto para:
- Clientes con **Préstamos Personales**.
- Clientes con **Tarjetas de Crédito**.

---

## 🛠️ Tecnologías Usadas

- Python 3.10+
- pandas
- numpy
- seaborn / matplotlib
- Jupyter Notebooks

---

## 🚀 Cómo usar

1. Ejecuta los notebooks correspondientes a cada producto.
2. Asegúrate de tener las bases segmentadas generadas por la etapa de preprocesamiento.
3. Explora las matrices de transición, el análisis de estados y los clústeres resultantes.

---

## 📌 Limitaciones

- Debido a la baja cantidad de observaciones por cliente (6 meses), muchas transiciones entre pares de estados no ocurren, lo cual impide construir una matriz irreducible por completo.
- Se optó por una segmentación de comportamiento en el siguiente paso (no convergente), lo cual sigue siendo útil para predicción y toma de decisiones en cobranza.