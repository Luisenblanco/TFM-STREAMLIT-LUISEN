
import pandas as pd
import streamlit as st

ruta_excel ="/mount/src/tfm-streamlit-luisen/Data/Datos_30_LIGAS.csv"

# Carga el archivo Excel y muestra las primeras filas
df = pd.read_csv(ruta_excel, encoding='latin', sep=";")

# Renombrar la columna 4510 a "Jugador"
df = df.rename(columns={"4510": "Jugador"})

with st.sidebar.expander("📊 METRICAS SELECCIONADAS"):
    # Multiselect para que el usuario seleccione las métricas
    metricas_seleccionadas = st.multiselect("SELECCIONE LAS MÉTRICAS", df.columns)
   
   
    st.write("Métricas seleccionadas:", metricas_seleccionadas)
   
with st.sidebar.expander("🥾⚽ LOS 6 JUGADORES A COMPARAR"):
    nombres_deseados = ['Cote', 'Pablo García', 'Rafel Obrador', 'Pablo Pérez', "D. van der Kust", 'S. Laquidaín']

    # Multiselect para que el usuario seleccione nombres
    nombres_seleccionados = st.multiselect("SELECCION DE JUGADORES:⚽", nombres_deseados)

# Filtrar el DataFrame por los nombres seleccionados
df_filtrado = df[df['Jugador'].isin(nombres_seleccionados)][metricas_seleccionadas]

st.title("📈GRAFICO DE LINEAS COMPARATIVA :⚽👟")
st.image("/mount/src/tfm-streamlit-luisen/Image/streamlit_logo.png", width=350)

# Mostrar el DataFrame en Streamlit
st.line_chart(df_filtrado)

st.image("/mount/src/tfm-streamlit-luisen/Image/sports.png", width=400)
st.image("/mount/src/tfm-streamlit-luisen/Image/FOTO MASTER.png", width=400)
