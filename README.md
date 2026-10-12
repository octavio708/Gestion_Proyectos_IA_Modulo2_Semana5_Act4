# Evaluación y Selección de Modelos Preentrenados (Hugging Face)

## 1. Descripción del Proyecto
Este repositorio contiene el prototipo técnico desarrollado para la materia **Gestión de Proyectos de Inteligencia Artificial (Módulo 2 / Semana 5)**. El caso de uso evalúa la implementación de tres modelos preentrenados de Hugging Face (`DistilBERT`, `RoBERTa` y `FinBERT`) para la clasificación automática de intenciones y urgencia en tickets de soporte financiero.

## 2. Entorno de Ejecución
* **Plataforma:** Google Colab con aceleración por hardware (GPU NVIDIA T4 / L4).
* **Librerías:** PyTorch, Transformers, Datasets, Scikit-learn, Pandas.
* **Instalación de Dependencias:** Ejecutar `pip install -r requirements.txt`.

## 3. Pasos de Ejecución
1. Clonar el repositorio.
2. Instalar las dependencias con `pip install -r requirements.txt`.
3. Abrir el archivo ubicado en `notebooks/evaluacion_modelos.ipynb`.
4. Configurar el entorno de ejecución de Colab para utilizar **GPU**.
5. Ejecutar las celdas secuencialmente para replicar la carga de datos, inferencia y cálculo de métricas.

## 4. Resultados y Métricas (Ejecución con GPU)
| Modelo | Accuracy | Precision (Weighted) | Recall (Weighted) | F1-Score (Weighted) | Latencia Media (ms) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **DistilBERT** | 0.30 | 0.3444 | 0.30 | 0.2227 | 32.72 ms |
| **RoBERTa** | 0.20 | 0.0667 | 0.20 | 0.1000 | 36.77 ms |
| **FinBERT** | 0.40 | 0.2222 | 0.40 | 0.2857 | 36.50 ms |

## 5. Conclusiones y Reflexión
* **Optimización por GPU:** El uso de GPU redujo la latencia de inferencia a un rango de **32 a 37 ms por consulta**, resolviendo los cuellos de botella temporales de procesamiento.
* **Desempeño Zero-Shot:** Los resultados reflejan que utilizar modelos sin ajuste fino (*fine-tuning*) y con barreras idiomáticas genera un rendimiento limitado, siendo **FinBERT** el que ofrece mejor afinidad con el dominio bancario.
* **Siguiente Fase:** Se propone realizar un proceso de *fine-tuning* supervisado con un dataset ampliado en español para escalar la precisión operativa a niveles de producción.

## 6. Estructura del Repositorio
- `data/`: Dataset original y procesado.
- `notebooks/`: Cuaderno funcional de prototipado.
- `src/`: Scripts de soporte modular.
- `results/`: Resumen tabular de métricas.