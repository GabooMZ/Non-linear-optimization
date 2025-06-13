# 🌲 Modelo Random Forest para Predicción de Pagos de Clientes

Este módulo contiene el entrenamiento y evaluación de modelos de regresión basados en **Random Forest**, diseñados para predecir cuánto pagará un cliente durante el próximo mes, utilizando como entrada su comportamiento en los últimos 5 meses. Se entrena un modelo por cada tipo de producto de crédito:

- 📌 **Préstamo Personal (PP)**
- 🛍️ **Tarjeta de Crédito Departamental (TDC_Dept)**
- 💳 **Tarjeta de Crédito Visa (TDC_Visa)**

---

## 📁 Contenido de la Carpeta

- `modelo_random_forest.ipynb`: Notebook principal donde se carga la información, se entrena cada modelo, y se evalúa su desempeño.
- 📂 Depende de los archivos preprocesados generados en la carpeta [`preprocesamiento_datos`](../preprocesamiento_datos/).

---

## 🧠 ¿Qué hace este modelo?

El modelo predice el **monto de pago mensual estimado** de cada cliente. Se utiliza el historial de los últimos 5 meses como variables predictoras. Se entrena un modelo distinto para cada tipo de producto financiero.

### 📈 Desempeño del Modelo (MAE - Mean Absolute Error)

| Producto        | MAE     |
|----------------|---------|
| Préstamo Personal (PP)    | **18.52** |
| TDC Departamental (TDC_Dept) | **7.77**  |
| TDC Visa (TDC_Visa)         | **19.48** |

---

## 🧾 Archivos de Entrada

Los modelos utilizan como entrada 3 archivos `.csv` generados durante la etapa de preprocesamiento:

- `PP_Segmentado_ABC.csv`
- `TDC_Dept_Segmentado_ABC.csv`
- `TDC_Visa_Segmentado_ABC.csv`

Para generar estos archivos, asegúrate de ejecutar primero el contenido de la carpeta [`preprocesamiento_datos`](../preprocesamiento_datos/).

---

## 🛠️ Tecnologías Usadas

- Python 3.10+
- pandas
- scikit-learn
- numpy
- matplotlib / seaborn (visualización)
- Jupyter Notebooks

---

## 🚀 Cómo usar

1. Asegúrate de tener los archivos `.csv` mencionados en la misma carpeta o directorio especificado.
2. Abre y ejecuta el notebook `modelo_random_forest.ipynb`.
3. Observa el entrenamiento, métricas de desempeño y la importancia de las variables por modelo.
4. (Opcional) Puedes ajustar hiperparámetros del modelo o cambiar la ventana temporal de entrada.

---

## 📌 Notas adicionales

- Todos los modelos son independientes y fueron entrenados por separado para mantener interpretabilidad y precisión por tipo de producto.
- El MAE es usado como métrica de evaluación para facilitar la comparación entre productos con distintos rangos de montos.
- La selección de variables se basa en las columnas resultantes del preprocesamiento de los últimos 5 meses históricos.
