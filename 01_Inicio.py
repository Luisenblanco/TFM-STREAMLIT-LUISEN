# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WOxkI3xjp64MBzgPGXT1gRVqlQOAnYIc
"""

import streamlit as st

st.set_page_config(
    page_title="Inicio",
    page_icon="⚽🥅",  # Corregido: Reemplazado "page_icons" por "page_icon"
    layout="wide"
)

st.sidebar.title("IV MASTER EN BIG DATA APLICADO AL SCOUTIG :⚽🥅")
st.sidebar.image("Image/sports.png", width=400)

  # Corregido: Reemplazado "with" por "width"
st.title("TFM CON STREAMLIT : LUISEN BLANCO ⚽🥅")
st.write("🎓 MASTER EN BIG DATA APLICADO AL SCOUTING 4 EDICION")
st.write("🥾⚽ **Sport Data Campus** | **Fecha del  Master** 1-03-2023 / 1-03-2024")
st.markdown(
    """<div style="background-color:#0C4DEE;height:10px;border-radius:5px;"></div>""",
    unsafe_allow_html=True
)


info = st.expander("DATOS PERSONALES", expanded=True)

with info:
    # Divide la fila en tres columnas
    col1, col2, col3 = st.columns([1, 2, 1])

    # Contenido de la primera columna
    with col1:
        st.write("LUIS ENRIQUE BLANCO SUAREZ | POLA DE LAVIANA(ASTURIAS)")
        st.write("✉️ CORREO ELECTRONICO - **luisenpola76@gmail.com**")
        st.write("🛸 PILOTO DE DRON | CATEGORIA A/1-A/3")
        st.write("🎥 VIDEO ANALISTA | EX-JUGADOR DEL REAL SPORTING DE GIJON")
        st.write("🎥 VIDEO ANALISIS CON NACSPORT")
        st.write("🙌 ENTRENADOR UEFA C")


    # Contenido de la segunda columna
    with col2:
         st.image("Image/LUISEN.jpg", width=250)

    with col3:
         st.image("Image/SPORTING.png", width=300)


st.markdown(
    """<div style="background-color:#0C4DEE;height:10px;border-radius:5px;"></div>""",
    unsafe_allow_html=True
)


menu_options = st.expander("OBJETIVO :🎯")
with menu_options:
    st.write("COMPARATIVA DE LOS 4 JUGADORES BUSCADOS CON **COTE**: 📊")
    st.write("👉 INTENTAREMOS DAR UN TOQUE MAS PROFESIONAL AL TFM")
    st.image("Image/sports.png", width=300)

st.markdown(
    """<div style="background-color:#0C4DEE;height:10px;border-radius:5px;"></div>""",
    unsafe_allow_html=True
)



menu_options = st.expander("JUGADORES A COMPARAR: 🥅")
# Crear un expander para los datos de los jugadores
with menu_options:
    # Divide la fila en cinco columnas
    col1, col2, col3, col4, col5 = st.columns(5)

    # Información del primer jugador (Cote)
    with col1:
        st.write("**COTE**")
        st.write("REAL SPORTING DE GIJON")
        st.image("Image/Cote.png", width=150)

    # Información del segundo jugador (D. van der Kust)
    with col2:
        st.write("**D. VAN DER KUST**")
        st.write("ESPARTA DE ROTERDAM")
        st.image("Image/Kust.png", width=250)

    # Información del tercer jugador (Pablo Perez)
    with col3:
        st.write("**PABLO PEREZ**")
        st.write("ATLETICO DE MADRID B")
        st.image("Image/Pablo.png", width=150)

    # Información del cuarto jugador (Rafel Obrador)
    with col4:
        st.write("**RAFAEL OBRADOR**")
        st.write("REAL MADRID B")
        st.image("Image/Obrador.png", width=250)

    # Información del quinto jugador (S. Laquidain)
    with col5:
        st.write("**S. LAQUIDAIN**")
        st.write("CA CENTRAL DE CORDOBA")
        st.image("Image/Laquidain.png", width=200)

st.markdown(
    """<div style="background-color:#0C4DEE;height:10px;border-radius:5px;"></div>""",
    unsafe_allow_html=True
)



menu_options = st.expander("DATOS Y PLATAFORMAS PARA EL TRABAJO:📊")
# Crear un expander para los datos de los jugadores
with menu_options:
    # Divide la fila en nueve columnas
    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

    # Imagen del primer recurso (Transfermarkt)
    with col1:
        st.image("Image/TRANSFERMARK.png", width=150)

    # Imagen del segundo recurso (Excel)
    with col2:
        st.image("Image/EXCEL.png", width=150)

    # Imagen del tercer recurso (Nacsport)
    with col3:
        st.image("Image/NACSPORT.png", width=200)

    # Imagen del cuarto recurso (Wyscout)
    with col4:
        st.image("Image/WYSCOUT.png", width=150)

    # Imagen del quinto recurso (R)
    with col5:
        st.image("Image/R.png", width=100)

    # Imagen del sexto recurso (Tableau)
    with col6:
        st.image("Image/TABLEAU.png", width=150)

    # Imagen del séptimo recurso (Python)
    with col7:
        st.image("Image/PYTHON.jpeg", width=100)

    # Imagen del octavo recurso (Power BI)
    with col8:
        st.image("Image/POWER BI.png", width=150)

    # Imagen del noveno recurso (Mediacoach)
    with col9:
        st.image("Image/MEDIACOACH.png", width=150)
  
