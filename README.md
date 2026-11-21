# Clasificación Supervisada de Consultas Médicas para la Red de Prestadores de Salud de Humana S.A.

Este repositorio contiene el proyecto final de la asignatura de **Aprendizaje Supervisado (Supervised Learning)**, diseñado a su vez como el componente fundacional del proyecto de titulación de grado (Capstone Project: *"Beyond SQL: Large Database Models for Intelligent Relational Data"*).

El sistema aborda las limitaciones de las consultas rígidas en bases de datos relacionales médicas mediante el modelado y clasificación de sintomatología en lenguaje natural hacia especialidades médicas, enlazando directamente las predicciones con la red privada de prestadores médicos de **Humana S.A.** en Ecuador.

---

## 📋 Estructura del Proyecto

```text
├── CAPSTONE_PROJECT.md         # Contexto, objetivos y vinculación con la tesis de grado
├── RUBRICS.md                  # Rúbrica oficial de evaluación del curso (10.0 pts)
├── README.md                   # Descripción general y guía de ejecución
├── proyectoFinal.ipynb         # Notebook Jupyter principal (End-to-End, 100% documentado)
├── web-scrapping-prestadores.py# Script de extracción automatizada de prestadores de Humana S.A.
├── data/                       # Almacenamiento local estructurado y caché
│   ├── prestadores_humana_limpio.csv       # Red de prestadores geolocalizados de Humana S.A.
│   ├── consultas_medicas_en.csv            # Dataset clínico en inglés (HPAI-BSC)
│   ├── consultas_medicas_es.csv            # Dataset clínico traducido y localizado al español
│   ├── embeddings_transfer_learning.npy    # Embeddings densos (384D) generados con MiniLM
│   ├── tsne_tfidf.npy                      # Proyección 2D t-SNE de TF-IDF + Chi2 (1500D)
│   └── tsne_transfer.npy                   # Proyección 2D t-SNE de Transfer Learning (384D)
└── img/                        # Diagramas e imágenes complementarias
```

---

## 🎯 Contenido y Cumplimiento de Rúbricas (10.0 / 10.0)

| Sección | Descripción Técnica en el Notebook | Rúbrica |
| :--- | :--- | :---: |
| **1. Introducción** | Motivación del problema: Búsqueda rígida en SQL vs. Enrutamiento semántico en Humana S.A., puente hacia Large Database Models (LDMs). | 0.1 pt |
| **2. EDA** | Arquitectura de doble adquisición (Mermaid), balance de clases, longitud de texto (palabras/caracteres), análisis léxico discriminativo (2x3). | 0.6 pt |
| **3. Feature Extraction** | Comparativa dual: TF-IDF con unigramas y bigramas (12,273 features) vs. Transfer Learning denso (384D) con `paraphrase-multilingual-MiniLM-L12-v2`. | 0.25 pt |
| **4. Feature Selection** | Filtro `SelectKBest(score_func=chi2, k=1500)` con reducción del 87.8% de dimensionalidad y gráfico del Top 20 términos clínicos informativos. | 0.25 pt |
| **5. Optimización de Hiperparámetros** | `RepeatedStratifiedKFold` (5 folds $\times$ 2 reps), curva de optimización de regularización $C$ ($\pm 1 \text{ std}$), curva de aprendizaje sesgo/varianza, y optimización Bayesiana con **Optuna**. | 3.5 pt |
| **6. Comparación Estadística de 2 Técnicas** | Validación cruzada pareada: TF-IDF + Chi2 + LogReg vs. Transfer Learning + MLP. Test de normalidad Shapiro-Wilk ($p=0.47$), Wilcoxon ($p=0.0195$) y t-test pareado ($p=0.0114$). Gráficos Boxplot y Slope Chart. | 3.5 pt |
| **7. Pipelines de Scikit-Learn** | Pipeline modular end-to-end (`TfidfVectorizer` $\rightarrow$ `SelectKBest` $\rightarrow$ `LogisticRegression`), evaluación sobre Hold-out Test Set (340 muestras), matriz de confusión, y función demostrativa `enrutar_consulta_humana`. | 0.5 pt |
| **8. Visualización t-SNE** | Reducción no lineal 2D con t-SNE sobre ambas representaciones vectoriales, gráficos duales 1x2 coloreados por especialidad supervisada e interpretación latente. | 1.0 pt |
| **9. Conclusiones** | 5 conclusiones estrictamente empíricas, cuantitativas y vinculadas a la práctica en Humana S.A. y al Capstone Project. | 0.1 pt |
| **10. Referencias & Idioma** | 11 referencias en formato IEEE cubriendo literatura médica, NLP, software y bases relacionales, más declaración de asistencia con IA. | 0.2 pt |

---

## 🚀 Requisitos e Instalación

Para ejecutar el notebook en un entorno local, se recomienda Python 3.10 o superior (compatible con Python 3.13):

```bash
# Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias requeridas
pip install pandas numpy matplotlib seaborn scikit-learn torch transformers optuna
```

---

## 🔬 Ejecución del Notebook

Abra el entorno de Jupyter o VS Code / Cursor / PyCharm y ejecute `proyectoFinal.ipynb`:

```bash
jupyter notebook proyectoFinal.ipynb
```

> **Nota de Rendimiento:** El notebook implementa persistencia y almacenamiento en caché para todas las etapas computacionalmente costosas (descarga, traducción, embeddings y t-SNE) dentro de la carpeta `data/`, garantizando una reproducción fluida y libre de bloqueos de rate limit.
