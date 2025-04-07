import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar y preparar datos
@st.cache_data
def cargar_datos():
    df = pd.read_csv("bd_medicacion.csv")
    df["Año"] = pd.to_numeric(df["Año"], errors="coerce")
    return df

df = cargar_datos()

st.title("📊 Visualización 3D Interactiva de Medicación")
st.markdown("Explora la evolución cruzando múltiples variables en un gráfico 3D animado.")

# --- Selección de variables para el gráfico ---
st.sidebar.header("⚙️ Configuración del gráfico 3D")

columnas = ["Año", "Sexo", "Edad", "Clase_social", "Categoría"]
eje_x = st.sidebar.selectbox("Eje X", columnas, index=0)
eje_y = st.sidebar.selectbox("Eje Y", columnas, index=1)
eje_z = st.sidebar.selectbox("Eje Z", columnas, index=2)
tamaño = st.sidebar.selectbox("Tamaño de los puntos", ["Personas"])
color = st.sidebar.selectbox("Color por", columnas, index=3)

# --- Filtros opcionales ---
st.sidebar.header("🎚️ Filtros")
categorias = st.sidebar.multiselect("Categorías", df["Categoría"].unique(), default=df["Categoría"].unique())
df_filtrado = df[df["Categoría"].isin(categorias)]

# --- Gráfico 3D con Plotly ---
st.write(f"### 🔍 Gráfico 3D: {eje_x} vs {eje_y} vs {eje_z}")

fig = px.scatter_3d(
    df_filtrado,
    x=eje_x,
    y=eje_y,
    z=eje_z,
    size=tamaño,
    color=color,
    animation_frame="Año",  # para ver la evolución por año
    opacity=0.7,
    title=f"Distribución de personas por {eje_x}, {eje_y}, {eje_z}",
    height=700
)

fig.update_traces(marker=dict(sizemin=3))
st.plotly_chart(fig)
