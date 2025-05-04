import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Visualización de Uso de Medicamentos en España")

@st.cache_data
def cargar_datos():
    df = pd.read_csv("medicamentoss_porcentual.csv")
    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return df

df = cargar_datos()

st.sidebar.header("Filtros")

quinquenal = st.sidebar.selectbox("Grupo de edad quinquenal", sorted(df["Quinquenal"].dropna().unique()))
subgrupo = st.sidebar.selectbox("Subgrupo farmacológico", sorted(df["Subgrupo Farmacológico"].dropna().unique()))
sexo = st.sidebar.selectbox("Sexo", sorted(df["Sexo"].dropna().unique()))
renta = st.sidebar.selectbox("Nivel de renta", sorted(df["Nivel Renta"].dropna().unique()))
laboral = st.sidebar.selectbox("Situación laboral", sorted(df["Situación Laboral"].dropna().unique()))
municipio = st.sidebar.selectbox("Tamaño del municipio", sorted(df["Tamaño Municipio"].dropna().unique()))
variable = st.sidebar.radio("Variable a visualizar", ["Porcentaje", "Personas con medicamento"])
anio = st.sidebar.selectbox("Año para comparación de medicamentos", sorted(df["Año"].unique()))

df_filtrado = df[
    (df["Quinquenal"] == quinquenal) &
    (df["Subgrupo Farmacológico"] == subgrupo) &
    (df["Sexo"] == sexo) &
    (df["Nivel Renta"] == renta) &
    (df["Situación Laboral"] == laboral) &
    (df["Tamaño Municipio"] == municipio)
]

if df_filtrado.empty:
    st.warning("No hay datos disponibles para la combinación seleccionada. Prueba con otros filtros.")
    st.stop()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Evolución anual")
    fig_line = px.line(
        df_filtrado,
        x="Año",
        y=variable,
        markers=True,
        labels={variable: variable},
        title="Tendencia a lo largo de los años"
    )
    st.plotly_chart(fig_line, use_container_width=True)

with col1:
    st.subheader("Comparativa por año")
    fig_bar = px.bar(
        df_filtrado,
        x="Año",
        y=variable,
        color="Año",
        labels={variable: variable},
        title="Valor por año"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    st.subheader("Comparativa por tipo de medicamento")

    df_meds = df[
        (df["Año"] == anio) &
        (df["Quinquenal"] == quinquenal) &
        (df["Sexo"] == sexo) &
        (df["Nivel Renta"] == renta) &
        (df["Situación Laboral"] == laboral) &
        (df["Tamaño Municipio"] == municipio)
    ]

    if df_meds.empty:
        st.info("No hay datos para mostrar todos los medicamentos con los filtros actuales.")
    else:
        fig_meds = px.bar(
            df_meds,
            x=variable,
            y="Subgrupo Farmacológico",
            orientation="h",
            color=variable,
            title=f"Uso de medicamentos por subgrupo en {anio}",
            labels={variable: variable},
            height=600
        )
        st.plotly_chart(fig_meds, use_container_width=True)

with col2:
    st.subheader("Mapa de calor por categorías")

    cat1 = st.selectbox("Variable en el eje X (categoría)", ["Sexo", "Nivel Renta", "Situación Laboral", "Tamaño Municipio", "Quinquenal"])
    cat2 = st.selectbox("Variable en el eje Y (categoría)", ["Sexo", "Nivel Renta", "Situación Laboral", "Tamaño Municipio", "Quinquenal"], index=1)

    subgrupo_farmacologico = st.selectbox("Selecciona un Subgrupo Farmacológico", df["Subgrupo Farmacológico"].unique())

    if cat1 == cat2:
        st.info("Selecciona dos variables diferentes para generar el gráfico de calor.")
    else:
        df_heat = df[
            (df["Año"] == anio) & 
            (df["Subgrupo Farmacológico"] == subgrupo_farmacologico)
        ]

        heat_data = df_heat.groupby([cat2, cat1])[variable].mean().reset_index()

        fig_heat = px.density_heatmap(
            heat_data,
            x=cat1,
            y=cat2,
            z=variable,
            color_continuous_scale="Viridis",
            labels={variable: f"Media de {variable}"},
            title=f"Mapa de calor de {variable} por {cat1} y {cat2} en {anio} para {subgrupo_farmacologico}"
        )

        st.plotly_chart(fig_heat, use_container_width=True)



st.markdown("---")
if st.checkbox("Mostrar tabla de datos filtrados"):
    st.dataframe(df_filtrado)
