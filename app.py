
import pandas as pd
import streamlit as st
import plotly.express as px

# Crear los datos (base completa)
data_full = [
    # ANSIOlÍTICOS.
    {"ATC": "N05BA01", "Principio_Activo": "Diazepam", "Grupo_ATC": "Derivados de la benzodiazepina", "DHDs": [9.22, 9.35, 9.73, 10.28, 11.12, 11.00, 10.61]},
    {"ATC": "N05BA05", "Principio_Activo": "Clorazepato de potasio", "Grupo_ATC": "Derivados de la benzodiazepina", "DHDs": [3.68, 3.58, 3.60, 3.60, 3.52, 3.38, 3.21]},
    {"ATC": "N05BA06", "Principio_Activo": "Lorazepam", "Grupo_ATC": "Derivados de la benzodiazepina", "DHDs": [22.11, 22.04, 21.98, 23.05, 23.22, 23.23, 22.53]},
    {"ATC": "N05BA08", "Principio_Activo": "Bromazepam", "Grupo_ATC": "Derivados de la benzodiazepina", "DHDs": [2.00, 2.06, 2.06, 2.10, 2.26, 2.26, 2.05]},
    {"ATC": "N05BA09", "Principio_Activo": "Clobazam", "Grupo_ATC": "Derivados de la benzodiazepina", "DHDs": [0.39, 0.38, 0.38, 0.38, 0.39, 0.39, 0.37]},
    {"ATC": "N05BA10", "Principio_Activo": "Ketazolam", "Grupo_ATC": "Derivados de la benzodiazepina", "DHDs": [1.19, 1.15, 1.11, 1.11, 1.10, 1.06, 1.03]},
    {"ATC": "N05BA12", "Principio_Activo": "Alprazolam", "Grupo_ATC": "Derivados de la benzodiazepina", "DHDs": [15.77, 15.46, 15.52, 15.16, 15.19, 15.65, 15.47]},
    {"ATC": "N05CD01", "Principio_Activo": "Flurazepam", "Grupo_ATC": "Hipnóticos y Sedantes", "DHDs": [0.75, 0.74, 0.73, 0.74, 0.75, 0.76, 0.19]},
    {"ATC": "N05CD06", "Principio_Activo": "Lormetazepam", "Grupo_ATC": "Hipnóticos y Sedantes", "DHDs": [21.95, 22.18, 22.5, 23.49, 24.06, 24.22, 34.37]},
    {"ATC": "N05CD08", "Principio_Activo": "Midazolam", "Grupo_ATC": "Hipnóticos y Sedantes", "DHDs": [0.22, 0.22, 0.21, 0.22, 0.21, 0.21, 0.20]},
    {"ATC": "N05CD11", "Principio_Activo": "Loprazolam", "Grupo_ATC": "Hipnóticos y Sedantes", "DHDs": [0.55, 0.54, 0.45, 0.45, 0.46, 0.45, 0.47]},
    {"ATC": "N05CF02", "Principio_Activo": "Zolpidem", "Grupo_ATC": "Fármacos relacionados con las benzodiazepinas", "DHDs": [7.24, 7.22, 7.27, 2.51, 7.64, 7.62, 7.64]},
    {"ATC": "N05CM02", "Principio_Activo": "Clometiazol", "Grupo_ATC": "Otros hipnóticos y sedantes", "DHDs": [0.22, 0.22, 0.22, 0.22, 0.22, 0.21, 0.20]},
    # ANTIDEPRESIVOS.
    {"ATC": "N06AA04", "Principio_Activo": "Clomipramina", "Grupo_ATC": "Inhibidores no selectivos de la recaptación de monoaminas", "DHDs": [0.85, 0.85, 0.86, 0.87, 0.88, 0.89, 0.89]},
    {"ATC": "N06AA09", "Principio_Activo": "Amitriptilina", "Grupo_ATC": "Inhibidores no selectivos de la recaptación de monoaminas", "DHDs": [1.77, 1.83, 1.93, 2.04, 2.22, 2.31, 2.37]},
    {"ATC": "N06AA21", "Principio_Activo": "Maprotilina", "Grupo_ATC": "Inhibidores no selectivos de la recaptación de monoaminas", "DHDs": [0.07, 0.07, 0.03, 0.02, 0.03, 0.04, 0.04]},
    {"ATC": "N06AB03", "Principio_Activo": "Fluoxetina", "Grupo_ATC": "Inhibidores selectivos de la recaptación de serotonina", "DHDs": [6.69, 6.80, 6.94, 7.06, 7.63, 7.99, 8.08]},
    {"ATC": "N06AB04", "Principio_Activo": "Citalopram", "Grupo_ATC": "Inhibidores selectivos de la recaptación de serotonina", "DHDs": [6.25, 6.18, 6.11, 6.09, 6.08, 5.95, 5.67]},
    {"ATC": "N06AB05", "Principio_Activo": "Paroxetina", "Grupo_ATC": "Inhibidores selectivos de la recaptación de serotonina", "DHDs": [9.07, 8.91, 8.80, 8.90, 9.00, 8.91, 8.61]},
    {"ATC": "N06AB06", "Principio_Activo": "Sertralina", "Grupo_ATC": "Inhibidores selectivos de la recaptación de serotonina", "DHDs": [12.64, 13.50, 14.56, 15.78, 17.34, 18.82, 19.81]},
    {"ATC": "N06AB10", "Principio_Activo": "Escitalopram", "Grupo_ATC": "Inhibidores selectivos de la recaptación de serotonina", "DHDs": [13.29, 13.31, 13.46, 13.88, 14.61, 14.96, 14.99]},
    {"ATC": "N06AX05", "Principio_Activo": "Trazodona", "Grupo_ATC": "Otros antidepresivos", "DHDs": [2.78, 2.96, 3.16, 3.38, 3.61, 3.84, 4.11]},
    {"ATC": "N06AX11", "Principio_Activo": "Mirtazapina", "Grupo_ATC": "Otros antidepresivos", "DHDs": [4.30, 4.50, 4.87, 5.16, 5.46, 5.75, 6.00]},
    {"ATC": "N06AX16", "Principio_Activo": "Venlafaxina", "Grupo_ATC": "Otros antidepresivos", "DHDs": [5.25, 5.36, 5.53, 5.84, 6.45, 6.82, 7.12]},
    {"ATC": "N06AX21", "Principio_Activo": "Duloxetina", "Grupo_ATC": "Otros antidepresivos", "DHDs": [5.22, 5.35, 5.54, 5.75, 6.11, 6.64, 7.12]},
    {"ATC": "N06AX23", "Principio_Activo": "Desvenlafaxina", "Grupo_ATC": "Otros antidepresivos", "DHDs": [3.25, 3.91, 4.46, 4.88, 5.24, 5.71, 6.00]},
    {"ATC": "N06AX26", "Principio_Activo": "Vortioxetina", "Grupo_ATC": "Otros antidepresivos", "DHDs": [0.92, 1.39, 1.98, 2.49, 3.15, 4.11, 5.06]},
    # ANTIPSICÓTICOS.
    {"ATC": "N05AA02", "Principio_Activo": "Levomepromazina", "Grupo_ATC": "Fenotiazinas con cadena laterala lifática", "DHDs": [0.11, 0.11, 0.11, 0.11, 0.11, 0.11, 0.09]},
    {"ATC": "N05AB03", "Principio_Activo": "Perfenazina", "Grupo_ATC": "Fenotiazinas con estructura piperidínica", "DHDs": [0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03]},
    {"ATC": "N05AE04", "Principio_Activo": "Ziprasidona", "Grupo_ATC": "Derivados del indol", "DHDs": [0.19, 0.17, 0.16, 0.15, 0.14, 0.13, 0.12]},
    {"ATC": "N05AF05", "Principio_Activo": "Zuclopentixol", "Grupo_ATC": "Derivados del tioxanteno", "DHDs": [0.14, 0.13, 0.13, 0.13, 0.13, 0.12, 0.11]},
    {"ATC": "N05AH03", "Principio_Activo": "Olanzapina", "Grupo_ATC": "Diazepinas, oxazepinas, tiazepinas y oxepinas", "DHDs": [2.60, 2.65, 2.69, 2.82, 2.92, 2.97, 3.03]},
    {"ATC": "N05AH04", "Principio_Activo": "Quetiapina", "Grupo_ATC": "Diazepinas, oxazepinas, tiazepinas y oxepinas", "DHDs": [2.17, 2.24, 2.31, 2.48, 2.61, 2.65, 2.73]},
    {"ATC": "N05AH06", "Principio_Activo": "Clotiapina", "Grupo_ATC": "Diazepinas, oxazepinas, tiazepinas y oxepinas", "DHDs": [0.21, 0.22, 0.22, 0.24, 0.25, 0.25, 0.26]},
    {"ATC": "N05AL05", "Principio_Activo": "Amisulprida", "Grupo_ATC": "Benzamidas", "DHDs": [0.28, 0.28, 0.27, 0.26, 0.26, 0.26, 0.25, 0.24]},
    {"ATC": "N05AN01", "Principio_Activo": "Litio", "Grupo_ATC": "Litio", "DHDs": [0.88, 0.88, 0.88, 0.89, 0.88, 0.87, 0.85]},    
    {"ATC": "N05AX08", "Principio_Activo": "Risperidona", "Grupo_ATC": "Otros antipsicóticos", "DHDs": [1.55, 1.49, 1.45, 1.44, 1.43, 1.40, 1.43]},
    {"ATC": "N05AX12", "Principio_Activo": "Aripiprazol", "Grupo_ATC": "Otros antipsicóticos", "DHDs": [1.24, 1.34, 1.41, 1.49, 1.57, 1.65, 1.73]},
    {"ATC": "N05AX13", "Principio_Activo": "Paliperidona", "Grupo_ATC": "Otros antipsicóticos", "DHDs": [1.75, 1.79, 1.86, 1.94, 1.98, 2.06, 2.03]}, 
]

# Expandir los registros en formato largo (una fila por a�o)
records = []
years = list(range(2017, 2024))

for entry in data_full:
    for year, dhd in zip(years, entry["DHDs"]):
        records.append({
            "ATC": entry["ATC"],
            "Principio_Activo": entry["Principio_Activo"],
            "Grupo_ATC": entry["Grupo_ATC"],
            "A�o": year,
            "DHD": dhd
        })

# Crear el DataFrame final
df_full = pd.DataFrame(records)

# Funci�n para clasificar la categor�a
def clasificar_categoria(atc):
    if atc.startswith("N05BA") or atc.startswith("N05CD") or atc.startswith("N05CF") or atc.startswith("N05CM"):
        return "Ansiol�ticos"
    elif atc.startswith("N06A"):
        return "Antidepresivos"
    elif atc.startswith("N05A"):
        return "Antipsic�ticos"
    else:
        return "Otros"

# A�adir la nueva columna de categor�a
df_full["Categor�a"] = df_full["ATC"].apply(clasificar_categoria)

# Cargar los datos a la app de Streamlit
st.title("Dashboard de Consumo de Medicamentos (2017-2023)")

# Sidebar para filtros
st.sidebar.header("Filtros")
categorias = df_full["Categor�a"].unique().tolist()
categoria_seleccionada = st.sidebar.selectbox("Selecciona una categor�a", categorias)

# Filtro por principio activo
principios = df_full[df_full["Categor�a"] == categoria_seleccionada]["Principio_Activo"].unique()
principio_seleccionado = st.sidebar.selectbox("Selecciona un principio activo", principios)

# Mostrar la evoluci�n temporal
st.subheader(f"Evoluci�n del consumo de {principio_seleccionado}")
df_filtrado = df_full[df_full["Principio_Activo"] == principio_seleccionado]
fig_line = px.line(df_filtrado, x="A�o", y="DHD", markers=True)
st.plotly_chart(fig_line)

# Mostrar el ranking de consumo en 2023
st.subheader(f"Top 10 {categoria_seleccionada.lower()} m�s consumidos en 2023")
df_2023 = df_full[(df_full["A�o"] == 2023) & (df_full["Categor�a"] == categoria_seleccionada)]
top_10 = df_2023.sort_values("DHD", ascending=False).head(10)
fig_bar = px.bar(top_10, x="DHD", y="Principio_Activo", orientation="h")
st.plotly_chart(fig_bar)

# Mostrar gr�fico de pastel por categor�a
st.subheader("Distribuci�n del consumo por categor�a en 2023")
df_2023_total = df_full[df_full["A�o"] == 2023].groupby("Categor�a")["DHD"].sum().reset_index()
fig_pie = px.pie(df_2023_total, values="DHD", names="Categor�a")
st.plotly_chart(fig_pie)
