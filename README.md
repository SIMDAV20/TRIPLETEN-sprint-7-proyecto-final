# TRIPLETEN-sprint-7-proyecto-final
Proyecto Final del sprint7 Bootcamp Tripleten

# Descripción del proyecto

Este proyecto es una aplicación web interactiva desarrollada con **Streamlit** para el análisis y visualización de datos de vehículos usados. La aplicación permite a los usuarios explorar un conjunto de datos de anuncios de venta de coches mediante gráficos interactivos.

## 🚗 **Características principales:**

- **Análisis exploratorio de datos (EDA)**: Notebook Jupyter con análisis detallado del dataset de vehículos
- **Visualizaciones interactivas**: Gráficos generados con Plotly Express
- **Interfaz web amigable**: Aplicación Streamlit con controles intuitivos
- **Dos tipos de visualización**:
  - **Histograma**: Distribución del odómetro (kilometraje) de los vehículos
  - **Gráfico de dispersión**: Relación entre odómetro y precio

## 📊 **Tecnologías utilizadas:**

- **Python**: Lenguaje de programación principal
- **Streamlit**: Framework para crear aplicaciones web
- **Pandas**: Manipulación y análisis de datos
- **Plotly Express**: Generación de gráficos interactivos
- **Jupyter Notebook**: Análisis exploratorio de datos

## 📁 **Estructura del proyecto:**

```
├── notebooks/
│   ├── EDA.ipynb              # Análisis exploratorio de datos
│   ├── app.py                 # Aplicación principal con botones
│   ├── app_checkboxes.py      # Versión alternativa con checkboxes
│   └── vehicles_us.csv        # Dataset de vehículos
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Documentación del proyecto
```
# Instalar las librerias o dependencias para ejecutar el proyecto

1. Ejecutar el siguiente comando en tu Anaconda Prompt
    
    ````````````
    pip install -r requirements.txt
    ````````````

2. Si quieres trabajar con el streamlit desde el app.py, ejecuta lo siguiente
    `````````````
    streamlit run app.py
    `````````````
