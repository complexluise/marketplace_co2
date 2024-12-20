import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
import numpy as np
from PIL import Image
import webbrowser


st.title("Net Zeo 2")

st.title("COSTA AZUL WIND PARK")

# Dividir la pantalla en cuatro columnas
col1, col2, col3, col4 = st.columns(4)

with col1:
    image5 = Image.open("../images/obj/f5.JPG")
    st.image(image5, caption="Location BOG-COL")

with col2:
    image6 = Image.open("../images/obj/f6.JPG")
    st.image(image6, caption="Industry Energy")

with col3:
    image7 = Image.open("../images/obj/f7.JPG")
    st.image(image7, caption="Methodology vcs")

with col4:
    image8 = Image.open("../images/obj/f8.JPG")
    st.image(image8, caption="Generated Bonds 400")


image9 = Image.open("../images/obj/f9.JPG")
st.image(image9, caption="NET ZEO 2")

st.header("about")
st.write(
    "Installation and operation of wind turbines to generate clean and renewable energy."
)
#################3#


df3 = pd.read_csv("../tabla3.csv")
df3.head()
print(df3)


# Crear un recuadro para seleccionar una opción
opcion_elegida = st.selectbox("Selecciona una opción:", df3["Nombre de proyecto"])
fila_seleccionada = df3[df3["SDG "] == opcion_elegida]

# valor_otra_columna = fila_seleccionada['SDG '].iloc[0]
# Mostrar el resultado en la página web

st.header("Resultado para la opción seleccionada:")
st.write(fila_seleccionada)

col1, col2 = st.columns(2)

# Agregar contenido a la primera columna
with col1:
    st.header("Columna 1")
    st.write("Este es el contenido de la primera columna.")


# Agregar contenido a la segunda columna
with col2:
    st.header("Columna 2")
    st.write("Este es el contenido de la segunda columna.")


st.title("For a Sustainable Future")
st.write(
    "Join the mission to change the world. Together, we work towards a sustainable future aligned with the United Nations Sustainable Development Goals, (SDG). Discover how you can make a difference today."
)

st.header("Sustainable development goals")
st.write(
    "Reduce your environmental impact by aligning your approach with the Sustainable Development Goals (SDG)."
)

image10 = Image.open("../images/obj/f10.JPG")
st.image(image10)

url = "https://github.com/complexluise/marketplace_co2/blob/main/Parte1.py"

# Botón para redirigir a la URL
if st.button("Buy Carbon Credits"):
    webbrowser.open_new_tab(url)

st.title("This project focuses on three sustainability goals.")

image11 = Image.open("../images/obj/f11.JPG")
st.image(image11)
st.header("SDG 7")
st.write(
    "Ensure access to affordable, reliable, sustainable, and modern energy for all."
)

image12 = Image.open("../images/obj/f12.JPG")
st.image(image12)
st.header("SDG 11")
st.write("Make cities and human settlements inclusive, safe, resilient.")


image13 = Image.open("../images/obj/f13.JPG")
st.image(image13)
st.header("SDG 13")
st.write("Take urgent action to combat climate change and its impacts.")

# Botón para redirigir a la URL
url2 = "https://github.com/complexluise/marketplace_co2/blob/main/Parte1.py"
if st.button("Buy Carbon Credits."):
    webbrowser.open_new_tab(url2)
