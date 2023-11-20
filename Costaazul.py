import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
import numpy as np
from PIL import Image
import webbrowser
from utils.extract_from_sheets import get_projects
from streamlit import connection

from geopy.geocoders import Nominatim
import pycountry

st.title("Net Zeo 2")

st.title("COSTA AZUL WIND PARK")

# Dividir la pantalla en cuatro columnas
col1, col2, col3, col4 = st.columns(4)

with col1:
    image5 = Image.open("Images/f5.JPG")
    st.image(image5, caption="Location BOG-COL")

with col2:
    image6 = Image.open("Images/f6.JPG")
    st.image(image6, caption="Industry Energy")

with col3:
    image7 = Image.open("Images/f7.JPG")
    st.image(image7, caption="Methodology vcs")

with col4:
    image8 = Image.open("Images/f8.JPG")
    st.image(image8, caption="Generated Bonds 400")


image9 = Image.open("Images/f9.JPG")
st.image(image9, caption="NET ZEO 2")

# Lista de datos
df3 = get_projects()  # Reemplaza con la ruta de tu archivo CSV
#df3 = df3.iloc[:-1]

#Nombres de las columnas del anterior dataframe
nombres_columnas3 = df3.columns

# Crear un recuadro para seleccionar una opción
opcion_elegida = st.selectbox("Selecciona una opción:", df3[nombres_columnas3[0]])
fila_seleccionada = df3.loc[df3[nombres_columnas3[0]] == opcion_elegida, nombres_columnas3[1]].iloc[0]
Description = df3.loc[df3[nombres_columnas3[0]] == opcion_elegida, nombres_columnas3[4]].iloc[0]
En = df3.loc[df3[nombres_columnas3[0]] == opcion_elegida, nombres_columnas3[2]].iloc[0]
Location = df3.loc[df3[nombres_columnas3[0]] == opcion_elegida, nombres_columnas3[3]].iloc[0]
sdgs_table = df3.loc[df3[nombres_columnas3[0]] == opcion_elegida, nombres_columnas3[5]].iloc[0]

def convertir_a_tupla(coordenadas_str):
    try:
        latitud, longitud = map(float, coordenadas_str.split(','))
        return (latitud, longitud)
    except ValueError:
        return None

# Ejemplo de uso: (40.7128, -74.0060)
input_text = Location
coordinates_transformed = convertir_a_tupla(input_text)


print(coordinates_transformed)

geolocator = Nominatim(user_agent="app")
location = geolocator.reverse(coordinates_transformed)
country_code = location.raw['address']['country_code']
country_name = pycountry.countries.get(alpha_2=country_code).name
#city_name = location.raw['address']['city']

st.header("Resultado para la opción seleccionada:")
st.write(fila_seleccionada)
st.write(En)
st.write(Description)

col1, col2 = st.columns(2)

# Agregar contenido a la primera columna
with col1:
    #Description = df3.loc[df3['Nombre de proyecto'] == opcion_elegida, 'Descripcion '].iloc[0]
    st.header("About")
    st.write(Description)

    geolocator = Nominatim(user_agent="app")
    location = geolocator.reverse(coordinates_transformed)
    country_code = location.raw['address']['country_code']
    country_name = pycountry.countries.get(alpha_2=country_code).name
    #city_name = location.raw['address']['city']

    coo = "Coordenadas"
    Pais = "País" 
    Ciudad_1 = "Ciudad"
    st.info(f"**{coo}**: {Location}")
    st.info(f"**{Pais}**: {country_name}")
    #st.info(f"**{Ciudad_1}**: {city_name}")

    country_code_lower = country_code.lower()
    flag_url = f"https://www.countryflags.io/{country_code_lower}/flat/64.png"
    st.image(flag_url, caption=f"Bandeira de {country_name}")

# Agregar contenido a la segunda columna
with col2:
    st.header(f"Mapa de {country_name}")
    ct_coordinates = coordinates_transformed

# Crear un DataFrame con las coordenadas de Bogotá
    data = {
    'LATITUDE': [ct_coordinates[0]],
    'LONGITUDE': [ct_coordinates[1]]
    }
    df = pd.DataFrame(data)

# Mostrar el mapa en Streamlit con st.map()
    st.map(df, zoom=11)





st.title("Details")

Proyecto = "Nombre del proyecto"
st.info(f"**{Proyecto}**: {opcion_elegida}")

Localizacion_proyecto = "Localización Proyecto"
st.info(f"**{Localizacion_proyecto}**: {country_name}")

Industria_tipo = "Tipo de industría"
st.info(f"**{Industria_tipo}**: {fila_seleccionada}")

sdg_proyecto = "Lista de SDG"
st.info(f"**{sdg_proyecto}**: {sdgs_table}")

Encabezado = "Encabezado serial"
st.info(f"**{Encabezado}**: {En}")


st.header("Sustainable development goals")
st.write(
    "Reduce your environmental impact by aligning your approach with the Sustainable Development Goals (SDG)."
)

image10 = Image.open("Images/f10.JPG")
st.image(image10)

url = "https://github.com/complexluise/marketplace_co2/blob/main/Parte1.py"

# Botón para redirigir a la URL
if st.button("Buy Carbon Credits"):
    webbrowser.open_new_tab(url)

st.title("This project focuses on three sustainability goals.")

col1, col2 = st.columns(2)

with col1:
    image11 = Image.open("Images/f11.JPG")
    st.image(image11)
    image12 = Image.open("Images/f12.JPG")
    st.image(image12)
    image13 = Image.open("Images/f13.JPG")
    st.image(image13)

with col2:
    st.header("SDG 7")
    st.write(
    "Ensure access to affordable, reliable, sustainable, and modern energy for all."
    )
    st.header("SDG 11")
    st.write("Make cities and human settlements inclusive, safe, resilient.")
    st.header("SDG 13")
    st.write("Take urgent action to combat climate change and its impacts.")



# Botón para redirigir a la URL
url2 = "https://github.com/complexluise/marketplace_co2/blob/main/Parte1.py"
if st.button("Buy Carbon Credits."):
    webbrowser.open_new_tab(url2)
