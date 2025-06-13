# 🧠 Modelo de Red Neuronal (Perceptrón Multicapa)

Este módulo contiene la implementación de una **red neuronal multicapa** (MLP - Multilayer Perceptron) entrenada para predecir el **monto que un cliente pagará en el siguiente mes**, utilizando como entrada su comportamiento histórico en los últimos 5 meses.

---

## 📁 Contenido de la Carpeta

- `neural_network.ipynb`: Notebook principal donde se realiza la construcción, entrenamiento y evaluación de la red neuronal para cada producto.

---

## 🧭 Objetivo

Construir un modelo predictivo con **capacidad no lineal** que complemente los enfoques tradicionales como Random Forest, permitiendo detectar patrones más complejos en los pagos de los clientes.

---

## 📥 Datos de Entrada

La red neuronal utiliza como entrada los archivos `.csv` generados en el módulo de [`preprocesamiento_datos`](../preprocesamiento_datos), específicamente:

- `PP_Segmentado_ABC.csv`
- `TDC_Dept_Segmentado_ABC.csv`
- `TDC_Visa_Segmentado_ABC.csv`

Cada archivo contiene datos históricos por cliente con variables preseleccionadas, normalizadas y estructuradas para aprendizaje supervisado.

---

## ⚙️ Arquitectura del Modelo

- Tipo: **Multilayer Perceptron (MLP)**
- Framework: `tensorflow.keras.models` (`Sequential`)
- Función de activación: ReLU
- Optimizador: Adam
- Arquitectura de la red:
```
Sequential([
    Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(16, activation='relu'),
    Dense(8, activation='relu'),
    Dense(4, activation='relu'),
    Dense(1)  # Salida para regresión
])
```

---

## 📊 Resultados de Desempeño

Los modelos fueron entrenados y evaluados para cada producto por separado, obteniendo los siguientes errores absolutos medios (MAE):

| Producto           | MAE    |
|--------------------|--------|
| Préstamo Personal  | 38.49  |
| TDC Departamental  | 8.31   |
| TDC Visa           | 39.81  |

> ⚠️ Aunque el desempeño es menor al obtenido por Random Forest, el modelo sirve como contraste y punto de partida para futuras mejoras con redes más profundas o redes recurrentes.

---

## 🛠️ Tecnologías Usadas

- Python 3.10+
- scikit-learn
- pandas
- numpy
- matplotlib / seaborn
- Jupyter Notebooks

---

## 🚀 Cómo usar

1. Asegúrate de haber ejecutado el módulo de preprocesamiento para obtener los archivos `.csv` de entrada.
2. Abre y corre el notebook `neural_network.ipynb`.
3. Explora los resultados, gráficas de pérdida, predicciones y métricas por producto.