# 📈 Modelo Bayesiano de Recuperación de Deuda

Este módulo implementa un enfoque probabilístico basado en **modelos bayesianos** para estimar la probabilidad de recuperación de deuda de los clientes. A diferencia de los modelos deterministas, este modelo permite capturar la **incertidumbre inherente** en el comportamiento de pago, así como actualizar dinámicamente las predicciones conforme llegan nuevos datos.

---

## 📁 Contenido de la Carpeta

| Archivo | Descripción |
|--------|-------------|
| `Prep Modelo Bayesiano PP.ipynb` | Preprocesamiento para Préstamos Personales |
| `Prep Modelo Bayesiano TDC Dept.ipynb` | Preprocesamiento para TDC Departamental |
| `Prep Modelo Bayesiano TDC Visa.ipynb` | Preprocesamiento para TDC Visa |
| `Modelo Bayesiano PP.qmd` | Implementación del modelo bayesiano en R para PP |
| `Modelo Bayesiano TDC Dept.qmd` | Implementación del modelo bayesiano en R para TDC Dept |
| `Modelo Bayesiano TDC Visa.qmd` | Implementación del modelo bayesiano en R para TDC Visa |

---

## 🧭 Objetivo

Estimar la **probabilidad de que un cliente recupere su nivel de pago** (o caiga en impago), incorporando la incertidumbre del sistema crediticio mediante métodos estadísticos rigurosos.

---

## 🎯 Justificación del Enfoque Bayesiano

Este enfoque se eligió por sus ventajas clave frente a modelos puramente frecuentistas:

- **📊 Incorporación de incertidumbre:**  
  Los parámetros del modelo son distribuciones aleatorias. Esto permite **cuantificar la variabilidad** en los coeficientes y obtener intervalos creíbles en vez de puntos estimados.

- **🛡️ Regularización mediante priors:**  
  La inclusión de **distribuciones a priori** permite reducir el sobreajuste, guiar el modelo con conocimiento experto y seleccionar automáticamente las variables más relevantes.

- **🔁 Actualización secuencial:**  
  El modelo puede ser **actualizado sin reentrenamiento completo**, integrando nuevos datos directamente en el marco bayesiano.

---

## 🔧 Procedimiento Estadístico

El modelo utiliza el algoritmo **MCMC (Markov Chain Monte Carlo)** para aproximar las distribuciones posteriores. Este procedimiento permite muestrear eficientemente los valores probables de los parámetros dada la información disponible, generando una representación completa de la incertidumbre en las predicciones.

---

## 📥 Datos de Entrada

Este módulo utiliza un preprocesamiento **específico** para este modelo (no los archivos generados en `/preprocesamiento_datos`). Cada producto tiene su notebook de preparación de datos:

- `Prep Modelo Bayesiano {PP, TDC Dept, TDC Visa}.ipynb`

---

## 🧪 Salida

Las salidas del modelo bayesiano incluyen:

- Distribuciones posteriores de los coeficientes
- Intervalos de credibilidad
- Probabilidades estimadas de pago/no pago
- Gráficas diagnósticas y de convergencia de cadenas

---

## 🛠️ Tecnologías Usadas

- Python 3.10 (preprocesamiento)
- R + Quarto (`.qmd`) para modelado:
  - `brms`
  - `tidyverse`, `mgcv`
- Algoritmos MCMC

---

## 🚀 Cómo usar

1. Corre el notebook de preprocesamiento correspondiente para generar los datos limpios.
2. Abre el archivo `.qmd` en RStudio o Quarto.
3. Ejecuta el modelo bayesiano para el producto deseado.
4. Interpreta los resultados y gráficas generadas al final del documento.

---

## 🧠 Nota Técnica

La calidad de los resultados depende de la **convergencia de las cadenas MCMC**, verificada mediante gráficos de trazado, `R̂`, y tamaño efectivo de muestra.
