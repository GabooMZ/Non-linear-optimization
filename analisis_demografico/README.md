# 🧑‍🤝‍🧑 Análisis Demográfico del Comportamiento de Pago

Esta carpeta contiene el análisis exploratorio del comportamiento de pago de los clientes según sus características demográficas. El objetivo es identificar patrones relevantes entre las variables demográficas y el cumplimiento de pago en distintos productos financieros.

---

## 📁 Contenido

- 📓 analisis_demografico.ipynb: Notebook principal donde se realiza el análisis exploratorio y visualización.
- 📊 Gráficas que relacionan género, estado y edad con el cumplimiento de pago.
- 📂 Utiliza las bases de datos segmentadas generadas en la carpeta [preprocesamiento_datos](../preprocesamiento_datos/).

---

## 🎯 Objetivo del Análisis

Evaluar cómo las características demográficas de los clientes —específicamente:

- 🧑‍🤝‍🧑 Género
- 🧭 Estado (entidad federativa)
- 🎂 Edad

impactan su comportamiento de pago en tres productos distintos:

1. Préstamo Personal (PP)
2. Tarjeta de Crédito Departamental (TDC_Dept)
3. Tarjeta de Crédito Visa (TDC_Visa)

---

## 🧾 Archivos de Entrada

El notebook utiliza como entrada los siguientes archivos .csv:
`
```
- PP_Segmentado_ABC.csv
- TDC_Dept_Segmentado_ABC.csv
- TDC_Visa_Segmentado_ABC.csv
```

Estos archivos deben ser generados previamente siguiendo los pasos descritos en la carpeta [preprocesamiento_datos](../preprocesamiento_datos/).

---

## 📈 Visualizaciones Generadas

El análisis incluye visualizaciones como:

- Barras de cumplimiento de pago por género
- Barras por estado
- Análisis por rangos de edad


Todas estas gráficas permiten identificar segmentos con mayor o menor propensión al pago.

---

## 🛠️ Herramientas Utilizadas

- Python 3.10+
- pandas
- matplotlib
- seaborn
- plotly (opcional para visualizaciones interactivas)
- Jupyter Notebooks

---

## 🚀 Cómo Ejecutar

1. Asegúrate de tener los archivos .csv de entrada en el mismo directorio.
2. Abre el archivo analisis_demografico.ipynb en Jupyter Notebook o Google Colab.
3. Ejecuta celda por celda para visualizar los análisis por producto y variable demográfica.

---

## 🧠 Conclusión

Este análisis ayuda a comprender cómo factores como la edad, el género y la ubicación geográfica pueden influir en el comportamiento de pago, facilitando la toma de decisiones en estrategias de cobranza segmentada.