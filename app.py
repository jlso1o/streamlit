import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar la página para que se despliegue horizontalmente
st.set_page_config(layout="wide")

# Título de la aplicación
st.title("Visualización Descriptiva del Conjunto de Datos Iris")

# Subtítulo
st.subheader("Análisis exploratorio de datos")

# Descripción o texto adicional
st.write("Esta aplicación permite realizar un análisis exploratorio de datos de forma interactiva. Elaborado por: Dr. José Luis Soto Ortiz")
st.write("Los datos fueron obtenidos de GitHub para su uso demostrativo.")

# Cargar datos desde GitHub
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
df = pd.read_csv(url)

# Sección 1: Mostrar los primeros registros y resumen estadístico
st.subheader("Datos del Conjunto de Iris")
col1, col2 = st.columns(2)  # Dividir la sección en dos columnas

with col1:
    st.write("Primeros 5 Registros")
    st.write(df.head())

with col2:
    st.write("Resumen Estadístico")
    st.write(df.describe())

# Sección 2: Histogramas y Gráficos de Dispersión
st.subheader("Visualizaciones Interactivas")
col3, col4 = st.columns(2)  # Dividir la sección en dos columnas

# Histograma en la primera columna
with col3:
    st.write("Histograma por característica")
    feature = st.selectbox("Selecciona una característica para graficar:", df.columns[:-1])
    fig = px.histogram(df, x=feature, nbins=20, title=f"Distribución de {feature}")
    st.plotly_chart(fig)

# Gráfico de dispersión en la segunda columna
with col4:
    st.write("Gráfico de Dispersión entre dos variables")
    x_axis = st.selectbox("Selecciona la variable del eje X", df.columns[:-1], key='xaxis')
    y_axis = st.selectbox("Selecciona la variable del eje Y", df.columns[:-1], key='yaxis')
    fig2 = px.scatter(df, x=x_axis, y=y_axis, color="species", title=f"Dispersión entre {x_axis} y {y_axis}")
    st.plotly_chart(fig2)
