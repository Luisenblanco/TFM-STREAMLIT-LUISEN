# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19ijPd0e-EmwVppsaITmhzHxYoag3Aw2p
"""

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt





ruta_excel ="/mount/src/tfm-streamlit-luisen/Data/Datos_30_LIGAS.csv"


# Carga el archivo Excel y muestra las primeras fila
df = pd.read_csv(ruta_excel, encoding='latin', sep=";")
print(df.head())

df = df.rename(columns={"4510": "Jugador"})

df.head()

# Eliminar las columnas no deseadas del DataFrame
columnas_a_eliminar = ['4510', 'Equipo', 'Equipo durante el periodo seleccionado', 'Posicion especifica', 'Edad', 'Valor de mercado(Transfermarkt)', 'Vencimiento de contrato']
df = df.drop(columns=columnas_a_eliminar, errors='ignore')

# Obtener todas las columnas del DataFrame después de eliminar las no 
cols_disponibles = df.columns.tolist()


with st.sidebar.expander("📊 METRICAS SELECCIONADAS"):
    # Multiselect para que el usuario seleccione las métricas
    metricas_seleccionadas = st.multiselect("SELECCIONE LAS MÉTRICAS", cols_disponibles)
    
    # Mostrar las métricas seleccionadas
    st.write("Métricas seleccionadas:", metricas_seleccionadas)

# Filtrar el DataFrame por los nombres deseados
nombres_deseados = ['Cote', 'Pablo García', 'Rafel Obrador', 'Pablo Pérez',"D. van der Kust", 'S. Laquidaín']
df_filtrado = df[df['Jugador'].isin(nombres_deseados)]

# Mostrar el DataFrame filtrado
print(df_filtrado)

import streamlit as st

with st.sidebar.expander("🥾⚽ LOS 6 JUGADORES A COMPARAR"):
    nombres_deseados = ['Cote', 'Pablo García', 'Rafel Obrador', 'Pablo Pérez', "D. van der Kust", 'S. Laquidaín']

    # Multiselect para que el usuario seleccione nombres
    nombres_seleccionados = st.multiselect("SELECCION DE JUGADORES:⚽", nombres_deseados)

    # Filtrar el DataFrame por los nombres seleccionados
    df_filtrado = df[df['Jugador'].isin(nombres_seleccionados)]
st.write(df_filtrado)

st.sidebar.image("/mount/src/tfm-streamlit-luisen/Image/sports.png", width=400)

if len(metricas_seleccionadas) == 2:
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(df_filtrado[metricas_seleccionadas[0]], df_filtrado[metricas_seleccionadas[1]], color='#0C48F6')  # Cambiar el color de los puntos a verde
    ax.set_title(f'📊GRAFICO DE DISPERSION: {metricas_seleccionadas[0]} vs {metricas_seleccionadas[1]}', fontsize=14, color='#0B0B0B')
    ax.set_xlabel(metricas_seleccionadas[0], fontsize=14, color='black')  # Cambiar el color y tamaño del eje x
    ax.set_ylabel(metricas_seleccionadas[1], fontsize=14, color='black')  # Cambiar el color y tamaño del eje y
    ax.set_facecolor('black')  # Cambiar el color del fondo del gráfico
    ax.grid(True)
    
    # Agregar el nombre de cada jugador en el gráfico
    for i, row in df_filtrado.iterrows():
        ax.text(row[metricas_seleccionadas[0]], row[metricas_seleccionadas[1]], row['Jugador'], fontsize=10, color='#6FF314', ha='center')
    
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)


else:
    st.write("👈⚽SELECCIONE DOS METRICAS:🥾⚽", width=450)
    
info = st.expander("SPORT DATA CAMPUS -STREAMLIT:🥾⚽")
with info:
    # Divide la fila en nueve columnas
    col1, col2 = st.columns(2)

    # Imagen del primer recurso (Transfermarkt)
    with col1:
        st.image("/mount/src/tfm-streamlit-luisen/Image/sports.png", width=250)

    # Imagen del segundo recurso (Excel)
    with col2:
        st.image("/mount/src/tfm-streamlit-luisen/Image/streamlit_logo.png", width=350)


