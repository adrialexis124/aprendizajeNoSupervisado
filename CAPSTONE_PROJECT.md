# Beyond SQL: Large Database Models for Intelligent Relational Data

Foundation models have transformed how machines learn from text, images, and code.
However, a vast amount of valuable real-world information remains stored in structured
and relational databases: customers, products, transactions, financial records,
scientific observations, healthcare records, and many other forms of interconnected data.

**Large Database Models (LDMs)** represent an emerging direction that seeks to bring
representation learning and foundation-model ideas directly into the database. Rather
than viewing database records simply as rows and columns to be queried through exact
conditions, these approaches learn vector representations (embeddings) that capture
relationships and similarities among entities, attributes, records, and potentially
multiple interconnected tables. Related research in **Relational Deep Learning (RDL)**
goes further by representing relational databases as heterogeneous graphs and learning
directly from their structure, reducing the need for extensive manual feature engineering.

This thesis project invites students to **explore, develop, evaluate, or extend machine
learning approaches for learning from relational databases**. The specific research
question, dataset, domain, and methodology can be defined by the student. Possible
directions include, but are not limited to:

### Recommendation and Similarity Systems

LDMs can learn representations of customers, products, transactions, or other entities
directly from structured data. Instead of relying exclusively on manually engineered
features or traditional collaborative filtering, a model could identify semantically
similar entities based on patterns distributed across multiple attributes. For example,
a retail database could support queries such as *"find customers similar to this
customer"* and use the resulting representations for personalized product recommendations,
customer segmentation, or next-purchase prediction.

### Semantic Search over Structured Data

Traditional SQL queries require users to specify precise conditions and relationships.
Learned database representations could enable **similarity-based or semantic retrieval**,
where records are retrieved according to their meaning or learned behavior rather than
only exact matches. A thesis could investigate how embedding-based retrieval compares
with conventional SQL queries, vector databases, or other semantic-search approaches.

### Fraud, Anomaly, and Behavioral Pattern Detection

Relational databases often contain complex interactions among customers, accounts,
transactions, devices, locations, or products. Representation learning over these
relationships could reveal unusual combinations or behaviors that are difficult to
capture using manually designed rules. Possible applications include fraud detection,
cybersecurity, financial risk, industrial monitoring, or other anomaly-detection problems.

### Relational Deep Learning and Foundation Models for Databases

A more methodological project could investigate models that learn directly from
**multiple interconnected tables**. Recent Relational Deep Learning approaches transform
relational databases into heterogeneous graphs, where rows become entities and
primary-key/foreign-key relationships define connections. Students could compare these
approaches with conventional tabular machine learning, develop new representation-learning
strategies, or explore whether representations learned from one database or task can
transfer to another.

### LDMs as a Data Layer for AI Agents

Another promising direction is the integration of structured-data representations with
**LLMs, Retrieval-Augmented Generation (RAG), or autonomous AI agents**. Instead of
providing an LLM only with retrieved text documents, an intelligent agent could retrieve
semantically related entities and relationships directly from enterprise databases.
Research could explore architectures combining database embeddings, relational models,
and LLMs to answer questions, support decisions, or interact with complex structured data.

These examples are intended to illustrate the breadth of the research area rather than
define a fixed thesis problem. **Students are encouraged to propose other applications,
datasets, domains, or methodological contributions related to learning representations
from structured and relational data.** Depending on the student's interests, the project
may emphasize model development, empirical benchmarking, representation learning,
database systems, or a domain-specific application.

## Starting References

1. **IBM — “Meet LDMs, the new (AI) sheriff in town.”**
    
    An accessible introduction to IBM's concept of Large Database Models and their use
    for learning from enterprise and transactional data.
    
    https://www.ibm.com/think/news/meet-large-database-models-ldms
    
2. **Fey, M., Hu, W., Huang, K., et al. (2024).
“Position: Relational Deep Learning — Graph Representation Learning on Relational Databases.”
ICML 2024.**
Introduces Relational Deep Learning (RDL), where relational databases are represented
as temporal heterogeneous graphs and learned end-to-end using graph neural networks.https://proceedings.mlr.press/v235/fey24a.html
3. **RelBench — Relational Deep Learning Benchmark.**
    
    A benchmark and software ecosystem containing real-world relational databases and
    predictive tasks for evaluating machine-learning approaches on relational data.
    
    https://github.com/snap-stanford/relbench
    
4. **Dwivedi, V. P., Kanatsoulis, C., Huang, S., & Leskovec, J. (2025).
“Relational Deep Learning: Challenges, Foundations and Next-Generation Architectures.”**
A broader review of RDL, its challenges, architectures, and its potential evolution
toward foundation models for relational data. https://arxiv.org/abs/2506.16654
5. **Chen, T., Kanatsoulis, C., & Leskovec, J. (2025).
“RelGNN: Composite Message Passing for Relational Deep Learning.”
ICML 2025.** https://arxiv.org/abs/2502.06784
Develops specialized graph-learning mechanisms for relational databases and evaluates
them across multiple real-world RelBench tasks.
6. **Wu, J., Thapa, R. B., Nayyeri, M., et al. (2026).
“Towards Foundation Models for Relational Databases with Language Models and
Graph Neural Networks.”**
Explores a hybrid architecture combining language-model representations of database
rows with graph neural networks that capture relationships between entities. https://arxiv.org/abs/2605.16085

### Aplicaciones de Interés

- Felipe destacó dos aplicaciones principales que le parecen relevantes:
    - **Semantic Search en datos tabulares:** consultar una base de datos SQL usando lenguaje natural, sin escribir SQL directamente
    - **Sistemas de recomendación:** encontrar clientes, registros o entidades similares a un perfil dado
- Se mencionó el proyecto **K-Pack** como posible fuente de datos estructurados para aplicar LDMs
- Para graduación, es suficiente aplicar el modelo a **cualquier dataset** (incluso sintético o SQL existente); no es obligatorio tener una aplicación novedosa

### Tema de Tesis

- El tema es **Beyond SQL / Large Database Models (LDMs)**, basado en un video de IBM revisado previamente
- El tema está **abierto** en cuanto a aplicación específica; Adrián debe proponer un caso de uso concreto
- Otros nombres equivalentes al concepto: **Relational Deep Learning (RDL)**

### Posibles Enfoques para Publicación

- Si se quiere publicar, se necesita una aplicación concreta o dataset relevante
- Alternativas válidas para un paper:
    - Encontrar una aplicación novedosa del modelo
    - Comparar varios enfoques/metodologías de LDMs en un dataset específico
    - Identificar una nueva forma de entrenar el modelo

### Proyecto del Curso Actual (Machine Learning)

- Adrián debe hacer un proyecto de **clasificación de texto** dentro del curso de aprendizaje supervisado
- El tema puede ser libre (e.g., clasificación de sentimientos), siguiendo la rúbrica del curso
- El objetivo es familiarizarse con el procesamiento de texto, relevante para la tesis
- Próximas clases del curso incluirán **transfer learning** (lunes) y un lab de redes neuronales (sábado)