#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt






ruta_excel ="/mount/src/tfm-streamlit-luisen/Data/Datos_30_LIGAS.csv"


# Carga el archivo Excel y muestra las primeras fila
df = pd.read_csv(ruta_excel, encoding='latin', sep=";")
print(df.head())





# Renombrar la columna 4510 a "Jugador"
df = df.rename(columns={"4510": "Jugador"})


# In[6]:
import streamlit as st

# Crear expander en la barra lateral
with st.sidebar.expander("VIDEOS COTE - PABLO GARCIA- PABLO PEREZ - S. LAQUIDAIN - VAN DER KUST - RAFAEL OBRADOR:⚽"):
    nombres_deseados = ['Cote', 'Pablo García']

    # Multiselect para que el usuario seleccione nombres
    nombres_seleccionados = st.multiselect("SELECCION DE JUGADORES:⚽", nombres_deseados)

    # Filtrar el DataFrame por los nombres seleccionados
    df_filtrado = df[df['Jugador'].isin(nombres_seleccionados)]
    st.write(df_filtrado)
   

st.title("📹VIDEOS COTE 🆚 PABLO GARCIA 🆚 PABLO PEREZ 🆚 S. LAQUIDAIN 🆚 VAN DER KUST 🆚 RAFAEL OBRADOR:⚽🥅")
st.image("/mount/src/tfm-streamlit-luisen/Image/streamlit_logo.png", width=350)
# Crear expander para los videos a la derecha
with st.expander("VIDEOS"):
    # Insertar los videos
    #video_file_pablo = open("C:/Users/user/Desktop/TFM-STREAMLIT/Video/Pablo Garcia.mp4", "rb")
    #video_bytes_pablo = video_file_pablo.read()
    
    st.video('https://youtu.be/-FRCEzFLUqY')

    #video_file_cote = open("C:/Users/user/Desktop/TFM-STREAMLIT/Video/Cote.mp4", "rb")
    #video_bytes_cote = video_file_cote.read()
    st.video("https://youtu.be/3kgS2uS3KZk")
    st.video("https://youtu.be/kaWKwK0gsFo")
    st.video("https://youtu.be/o0R_9RjuWsk?si=UD9pBSfWZxwR0CPS")
    st.video("https://youtu.be/9L8ivBS1_jo?si=nZXc4ScDR9NpaNux")

# Insertar imagen en la parte derecha
st.image("/mount/src/tfm-streamlit-luisen/Image/sports.png", width=400)



