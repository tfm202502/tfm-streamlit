import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
@st.cache_data
def cargar_datos():
    return pd.read_csv("bd_medicacion.csv")

df = cargar_datos()
df["Año"] = pd.to_numeric(df["Año"], errors='coerce')


st.title("Visualización Datos de Medicación por Variables Sociodemográficas")


st.sidebar.header("🎛️ Filtros")

anios = st.sidebar.multiselect("Año", sorted(df["Año"].unique()), default=sorted(df["Año"].unique()))
sexo = st.sidebar.multiselect("Sexo", df["Sexo"].unique(), default=df["Sexo"].unique())
clase = st.sidebar.multiselect("Clase social", df["Clase_social"].unique(), default=df["Clase_social"].unique())
edad = st.sidebar.multiselect("Edad", df["Edad"].unique(), default=df["Edad"].unique())


df_filtrado = df[
    df["Año"].isin(anios) &
    df["Sexo"].isin(sexo) &
    df["Clase_social"].isin(clase) &
    df["Edad"].isin(edad)
]

st.write("Datos filtrados")
st.dataframe(df_filtrado)


st.write("Personas por Categoría de Medicación")

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(data=df_filtrado, x="Categoría", y="Personas", estimator=sum, errorbar=None, palette="pastel", ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)


st.write("Evolución por Categoría de Medicación")

fig2, ax2 = plt.subplots(figsize=(10, 5))
categoria_group = df_filtrado.groupby(["Año", "Categoría"])["Personas"].sum().reset_index()
sns.lineplot(data=categoria_group, x="Año", y="Personas", hue="Categoría", marker="o", ax=ax2)
st.pyplot(fig2)


st.write("Evolución por Sexo")

fig3, ax3 = plt.subplots(figsize=(8, 5))
sexo_group = df_filtrado.groupby(["Año", "Sexo"])["Personas"].sum().reset_index()
sns.lineplot(data=sexo_group, x="Año", y="Personas", hue="Sexo", marker="o", ax=ax3)
st.pyplot(fig3)


st.write("Evolución por Clase Social")

fig4, ax4 = plt.subplots(figsize=(8, 5))
clase_group = df_filtrado.groupby(["Año", "Clase_social"])["Personas"].sum().reset_index()
sns.lineplot(data=clase_group, x="Año", y="Personas", hue="Clase_social", marker="o", ax=ax4)
st.pyplot(fig4)


st.write("Evolución por Grupos de Edades")

fig5, ax5 = plt.subplots(figsize=(8, 5))
edad_group = df_filtrado.groupby(["Año", "Edad"])["Personas"].sum().reset_index()
sns.lineplot(data=edad_group, x="Año", y="Personas", hue="Edad", marker="o", ax=ax5)
st.pyplot(fig5)

st.write("Sexo y Clase Social")

group_sexo_renta = df_filtrado.groupby(["Sexo", "Clase_social"])["Personas"].sum().reset_index()

fig6, ax6 = plt.subplots(figsize=(8, 5))
sns.barplot(data=group_sexo_renta, x="Clase_social", y="Personas", hue="Sexo", ax=ax6)
ax6.set_title("Personas por Clase Social y Sexo")
st.pyplot(fig6)


st.write("Sexo y Edad")

group_sexo_edad = df_filtrado.groupby(["Sexo", "Edad"])["Personas"].sum().reset_index()

fig7, ax7 = plt.subplots(figsize=(8, 5))
sns.barplot(data=group_sexo_edad, x="Edad", y="Personas", hue="Sexo", ax=ax7)
ax7.set_title("Personas por Edad y Sexo")
st.pyplot(fig7)


st.write("Edad y Clase Social")

group_edad_renta = df_filtrado.groupby(["Edad", "Clase_social"])["Personas"].sum().reset_index()

fig8, ax8 = plt.subplots(figsize=(10, 5))
sns.barplot(data=group_edad_renta, x="Edad", y="Personas", hue="Clase_social", ax=ax8)
ax8.set_title("Personas por Edad y Clase Social")
st.pyplot(fig8)

st.write("Mapa de calor Edad y Clase Social")

pivot = df_filtrado.pivot_table(
    index="Edad", columns="Clase_social", values="Personas", aggfunc="sum"
)

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu", ax=ax)
st.pyplot(fig)

