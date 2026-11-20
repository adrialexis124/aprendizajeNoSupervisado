# Requerimientos del Proyecto Final

A continuación se detallan los ítems a evaluar en el proyecto, su descripción y la puntuación máxima asignada:

1. **Introducción** (Puntuación Máxima: 0.1)
   - Realizar una introducción donde motive el problema a resolver y su importancia.

2. **EDA (Exploratory Data Analysis)** (Puntuación Máxima: 0.6)
   - Realizar un "Exploratory Data Analysis" de su dataset.

3. **Feature Extraction** (Puntuación Máxima: 0.25)
   - Para datasets con data no estructurada cuando se usa transfer learning.

4. **Feature Selection** (Puntuación Máxima: 0.25)
   - Implementar una técnica de feature selection (tipo filter) en su pipeline. En caso de usar transfer learning o si su problema es sobre imágenes o texto, pueden omitir este paso.

5. **Optimización de hiperparámetros** (Puntuación Máxima: 3.5)
   - Optimizar sus hiperparámetros en un conjunto de validación adecuado con `repeated k-fold cv`. Aunque se puede usar nested k-fold CV, **no se recomienda** porque la ejecución puede demorar considerablemente más.
   - Presentar una gráfica de la optimización de algún hiperparámetro de su modelo.
   - Presentar también la curva de aprendizaje.
   - *Opcional (extra):* usar Optuna (https://optuna.org).

6. **Comparación estadística de 2 técnicas ML** (Puntuación Máxima: 3.5)
   - Se debe realizar una comparación estadística entre dos técnicas de aprendizaje automático.
   - La comparación debe llevarse a cabo mediante un test de hipótesis apropiado (por ejemplo, Wilcoxon o t-test), utilizando *repeated k-fold cross-validation*.
   - Por defecto, se recomienda realizar **10 repeticiones con 10 folds** ($k=10$). Sin embargo, si este proceso resulta muy costoso computacionalmente, se puede reducir la validación a **2 repeticiones con 5 folds** ($k=5$).

7. **Pipelines** (Puntuación Máxima: 0.5)
   - Usar `pipelines` de sklearn. Si implementa una red neuronal, use las clases y métodos adecuados para que su código sea modular (e.g., clases de Lightning o PyTorch para estructurar modelos, data y entrenamientos en redes neuronales).

8. **Visualización con t-SNE** (Puntuación Máxima: 1.0)
   - Usar t-SNE para visualizar su espacio de características en 2 dimensiones. Si usa una técnica supervisada, usar el label como color del punto en la visualización.

9. **Idioma** (Puntuación Máxima: 0.1)
   - Uso del idioma (ortografía y redacción).

10. **Referencias** (Puntuación Máxima: 0.1)
    - Colocar referencias en formato IEEE tanto de los conceptos teóricos como del código fuente. Si usa ChatGPT para el código, colocar los prompts usados como comentarios de Python en el lugar apropiado.

11. **Conclusiones** (Puntuación Máxima: 0.1)
    - Redactar conclusiones pertinentes. Recordar que la teoría no es una conclusión.

---
**Puntaje Total:** 10.0
