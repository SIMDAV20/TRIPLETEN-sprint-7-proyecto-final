import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# Crear casillas de verificación
st.write('Selecciona los gráficos que deseas visualizar:')
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:  # si la casilla de verificación del histograma está seleccionada
    st.write('Construyendo un histograma para la columna odómetro')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:  # si la casilla de verificación del gráfico de dispersión está seleccionada
    st.write('Construyendo un gráfico de dispersión entre odómetro y precio')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
