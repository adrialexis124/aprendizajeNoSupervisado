# Clasificación Supervisada de Consultas Médicas para la Red de Prestadores de Salud de Humana S.A.

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/adrialexis124/aprendizajeNoSupervisado)

> **Repositorio Oficial en GitHub:** [https://github.com/adrialexis124/aprendizajeNoSupervisado](https://github.com/adrialexis124/aprendizajeNoSupervisado)

Este repositorio contiene el proyecto de la asignatura de **Aprendizaje Supervisado (Supervised Learning)**, enfocado en el modelado y clasificación de sintomatología en lenguaje natural hacia especialidades médicas, enlazando directamente las predicciones con la red privada de prestadores médicos de **Humana S.A.** en Ecuador.

El sistema aborda las limitaciones de las consultas rígidas en bases de datos relacionales médicas mediante técnicas modernas de procesamiento de lenguaje natural (NLP), aprendizaje supervisado y reducción de dimensionalidad, sentando las bases para sistemas de enrutamiento inteligente de pacientes y arquitecturas de bases de datos enriquecidas semánticamente.

---

## 📋 Estructura del Proyecto

```text
├── README.md                   # Descripción general, enlaces y guía de ejecución
├── requirements.txt            # Especificación completa de dependencias de Python
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

## 🎯 Contenido y Módulos Metodológicos del Notebook

| Sección | Descripción Técnica en el Notebook | Componentes Evaluados |
| :--- | :--- | :--- |
| **1. Introducción** | Motivación del problema: Búsqueda rígida en SQL vs. Enrutamiento semántico en Humana S.A., y puente hacia arquitecturas relacionales inteligentes. | Justificación de negocio y técnica |
| **2. EDA** | Arquitectura de doble adquisición (Mermaid), balance de clases, longitud de texto (palabras/caracteres), análisis léxico discriminativo (cuadrícula 2x3). | Análisis exploratorio riguroso |
| **3. Feature Extraction** | Comparativa dual: TF-IDF con unigramas y bigramas (12,273 features) vs. Transfer Learning denso (384D) con `paraphrase-multilingual-MiniLM-L12-v2`. | Representación dispersa vs. densa |
| **4. Feature Selection** | Filtro `SelectKBest(score_func=chi2, k=1500)` con reducción del 87.8% de dimensionalidad y gráfico del Top 20 términos clínicos informativos. | Reducción de dimensionalidad supervisada |
| **5. Optimización de Hiperparámetros** | `RepeatedStratifiedKFold` (5 folds $\times$ 2 reps), curva de optimización de regularización $C$ ($\pm 1 \text{ std}$), curva de aprendizaje sesgo/varianza, y optimización Bayesiana con **Optuna**. | Búsqueda exhaustiva y bayesiana |
| **6. Comparación Estadística de 2 Técnicas** | Validación cruzada pareada: TF-IDF + Chi2 + LogReg vs. Transfer Learning + MLP. Test de normalidad Shapiro-Wilk ($p=0.47$), Wilcoxon ($p=0.0195$) y t-test pareado ($p=0.0114$). Gráficos Boxplot y Slope Chart. | Pruebas de hipótesis estadísticas formales |
| **7. Pipelines de Scikit-Learn** | Pipeline modular end-to-end (`TfidfVectorizer` $\rightarrow$ `SelectKBest` $\rightarrow$ `LogisticRegression`), evaluación sobre Hold-out Test Set (340 muestras), matriz de confusión, y función demostrativa `enrutar_consulta_humana`. | Arquitectura modular de inferencia |
| **8. Visualización t-SNE** | Reducción no lineal 2D con t-SNE sobre ambas representaciones vectoriales, gráficos duales 1x2 coloreados por especialidad supervisada e interpretación latente. | Inspección cualitativa del espacio latente |
| **9. Conclusiones** | Conclusiones estrictamente empíricas, cuantitativas y vinculadas a la práctica clínica y operativa en Humana S.A. | Hallazgos basados en datos |
| **10. Referencias & Formato** | 11 referencias en formato IEEE cubriendo literatura médica, NLP, software y bases relacionales, más declaración de asistencia con IA. | Rigor académico y reproducibilidad |

---

## 🚀 Requisitos e Instalación

Para clonar y ejecutar el proyecto en un entorno local, se recomienda Python 3.10 o superior (probado y compatible con Python 3.13):

```bash
# 1. Clonar el repositorio
git clone https://github.com/adrialexis124/aprendizajeNoSupervisado.git
cd aprendizajeNoSupervisado

# 2. Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate  # En Linux/macOS
# .venv\Scripts\activate   # En Windows

# 3. Instalar dependencias desde requirements.txt
pip install -r requirements.txt
```

---

## 🔬 Ejecución del Notebook

Abra el entorno de Jupyter o su IDE preferido (VS Code, Cursor, PyCharm) y ejecute `proyectoFinal.ipynb`:

```bash
jupyter notebook proyectoFinal.ipynb
```

> **Nota de Rendimiento:** El notebook implementa persistencia y almacenamiento en caché para todas las etapas computacionalmente costosas (descarga, traducción, embeddings densos y proyecciones t-SNE) dentro de la carpeta `data/`, garantizando una reproducción fluida y libre de bloqueos de rate limit.
