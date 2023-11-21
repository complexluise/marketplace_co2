import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
import numpy as np
from PIL import Image
import webbrowser
#from utils.extract_from_sheets import get_projects
from geopy.geocoders import Nominatim
import pycountry
import re


st.set_page_config(
    page_title="Projects Detail",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)



#Lectura tercer dataframe
file_path3 = "tabla3.csv"  # Reemplaza con la ruta de tu archivo CSV
df3 = pd.read_csv(file_path3)
df3 = df3.iloc[:-1]

#Convertir a mayusculas para el titulo
def convertir_a_mayusculas(cadena):
    return cadena.upper()

opcion_elegida = st.selectbox("Select the project to consulting:", df3["Nombre de proyecto"])

Titulo_proy = convertir_a_mayusculas(opcion_elegida)

st.markdown("<h1 style='text-align: center; color: green;'>NETZEO2</h1>", unsafe_allow_html=True)




# Título centrado de color verde y tamaño grande

st.markdown(f"<h1 style='text-align: center; color: green;'>{Titulo_proy}</h1>", unsafe_allow_html=True)



fila_seleccionada = df3.loc[df3["Nombre de proyecto"] == opcion_elegida, "Industría"].iloc[0]
Description = df3.loc[df3["Nombre de proyecto"] == opcion_elegida, "Descripcion "].iloc[0]
En = df3.loc[df3["Nombre de proyecto"] == opcion_elegida, "Encabezado Serial"].iloc[0]
Location = df3.loc[df3["Nombre de proyecto"] == opcion_elegida, "Ubicacion "].iloc[0]
sdgs_table = df3.loc[df3["Nombre de proyecto"] == opcion_elegida, "SDG "].iloc[0]

#Convierte la cadena str de location a valores numericos
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

try:
    # Intenta acceder a la información en location
    country_code = location.raw['address']['country_code']
    country_name = pycountry.countries.get(alpha_2=country_code).name
    # Resto del código que utiliza country_code
except (AttributeError, KeyError):
    # Manejo de la excepción si hay un error al acceder a location.raw
    country_code = None  # Otra opción es asignar un valor por defecto o hacer algo diferente según tus necesidades
    country_name = None




# Dividir la pantalla en cuatro columnas
col1, col2, col3, col4 = st.columns(4)

#Lectura primer y segundo dataframe
#Lectura tercer dataframe
file_path1 = "tabla1.csv"  # Reemplaza con la ruta de tu archivo CSV
file_path2 = "tabla2.csv"  # Reemplaza con la ruta de tu archivo CSV
df1 = pd.read_csv(file_path1)
df2 = pd.read_csv(file_path2)


#Metodologia y bonos generados
vcs = df1.loc[df1["Nombre de Proyecto"] == opcion_elegida, "Metodología"].iloc[0]
bonos_generados = df1.loc[df1["Nombre de Proyecto"] == opcion_elegida, "Cantidad de Bonos generados"].iloc[0]

with col1:
    image5 = Image.open("images/obj/f5.JPG")
    st.image(image5, caption=f"Location:  {country_name}")

with col2:
    image6 = Image.open("images/obj/f6.JPG")
    st.image(image6, caption=f"Industry:  {fila_seleccionada}")

with col3:
    image7 = Image.open("images/obj/f7.JPG")
    st.image(image7, caption=f"Methodology: {vcs}")

with col4:
    image8 = Image.open("images/obj/f8.JPG")
    st.image(image8, caption=f"Generated Bonds: {bonos_generados}")


image9 = Image.open("images/obj/f9.JPG")
st.image(image9, caption="NET ZEO 2")

#Creación de dos columnas

col1, col2 = st.columns(2)

with col1:
    
    tamaño_letra = 40
    titulo_html = f"<h1 style='text-align: center; color: #001f3f; font-size: {tamaño_letra}px;'>About</h1>"
    st.markdown(titulo_html, unsafe_allow_html=True)


    st.write("Description of projects: ", Description)

    if opcion_elegida != "Parque Eólico Costa Azul":
        geolocator = Nominatim(user_agent="app")
        location = geolocator.reverse(coordinates_transformed)   
        country_code = location.raw['address']['country_code']
        country_name = pycountry.countries.get(alpha_2=country_code).name  
    else:
        location = coordinates_transformed
        country_name = coordinates_transformed

    coo = "Coordinates"
    Pais = "Country" 
    
    st.info(f"**{coo}**: {Location}")

    Proyecto = "Project Name"
    st.info(f"**{Proyecto}**: {opcion_elegida}")

    #
    if opcion_elegida != "Parque Eólico Costa Azul":
        Localizacion_proyecto = "Location Project"
        st.info(f"**{Localizacion_proyecto}**: {country_name}")
    #

    Industria_tipo = "Industry Type"
    st.info(f"**{Industria_tipo}**: {fila_seleccionada}")

    sdg_proyecto = "List SDG"
    st.info(f"**{sdg_proyecto}**: {sdgs_table}")

    Encabezado = "Serial"
    st.info(f"**{Encabezado}**: {En}")

    

# Agregar contenido a la segunda columna
with col2:
    tamaño_letra = 40
    titulo_html = f"<h1 style='text-align: center; color: #001f3f; font-size: {tamaño_letra}px;'>Mapa of {country_name}</h1>"
    st.markdown(titulo_html, unsafe_allow_html=True)

    ct_coordinates = coordinates_transformed

# Crear un DataFrame con las coordenadas de Bogotá
    data = {
    'LATITUDE': [ct_coordinates[0]],
    'LONGITUDE': [ct_coordinates[1]]
    }
    df = pd.DataFrame(data)

# Mostrar el mapa en Streamlit con st.map()
    st.map(df, zoom=11)

tamaño_letra = 50
titulo_html = f"<h1 style='text-align: center; color: #001f3f; font-size: {tamaño_letra}px;'>More information</h1>"
st.markdown(titulo_html, unsafe_allow_html=True)

prov = df1.loc[df1["Nombre de Proyecto"] == opcion_elegida, "Proveedor (Nombre del representante legal del proyecto)"].iloc[0]
entity = df1.loc[df1["Nombre de Proyecto"] == opcion_elegida, "Entidad verificadora"].iloc[0]
g_b = df1.loc[df1["Nombre de Proyecto"] == opcion_elegida, "Cantidad de Bonos generados"].iloc[0]
b_p = df1.loc[df1["Nombre de Proyecto"] == opcion_elegida, "Bonos en paquetes"].iloc[0]
b_d = df1.loc[df1["Nombre de Proyecto"] == opcion_elegida, "Bonos Disponibles"].iloc[0]
n_s = df1.loc[df1["Nombre de Proyecto"] == opcion_elegida, "Número serial de bonos"].iloc[0]
stt = df1.loc[df1["Nombre de Proyecto"] == opcion_elegida, "Status"].iloc[0]

Localizacion_proyecto = "Provider"
st.info(f"**{Localizacion_proyecto}**: {country_name}")

Industria_tipo = "Verification Entity"
st.info(f"**{Industria_tipo}**: {entity}")

sdg_proyecto = "Methodology"
st.info(f"**{sdg_proyecto}**: {vcs}")

generated_bones = "Generated bonds"
st.info(f"**{generated_bones}**: {g_b}")

bones_pk = "Bonds in a Package"
st.info(f"**{bones_pk}**: {b_p}")

available = "Available Bonds"
st.info(f"**{available}**: {b_d}")

ser="Serial Number"
st.info(f"**{ser}**: {n_s}")

status_type="Status"
st.info(f"**{status_type}**: {stt}")

title_sdg = convertir_a_mayusculas("Sustainable development goals")

st.markdown(f"<h1 style='text-align: center; color: pink;'>{title_sdg}</h1>", unsafe_allow_html=True)

texto_html = """
    <div style='text-align: center; font-size: 24px;'>
        <p style='text-align: justify;'>
            The 2030 Agenda for Sustainable Development, adopted by all United Nations Member States in 2015, provides a shared blueprint for peace and prosperity for people and the planet, now and into the future. At its heart are the 17 Sustainable Development Goals (SDGs), which are an urgent call for action by all countries - developed and developing - in a global partnership. They recognize that ending poverty and other deprivations must go hand-in-hand with strategies that improve health and education, reduce inequality, and spur economic growth – all while tackling climate change and working to preserve our oceans and forests.
        </p>
    </div>
"""
st.markdown(texto_html, unsafe_allow_html=True)

url="https://sdgs.un.org/goals"
if st.button("Learn more about the Sustainable Development Goals."):
    webbrowser.open_new_tab(url)



col1, col2, col3, col4, col5, col6 = st.columns(6)

obj1=Image.open("images/sdg/1.JPG")
obj2=Image.open("images/sdg/2.JPG")
obj3=Image.open("images/sdg/3.JPG")
obj4=Image.open("images/sdg/4.JPG")
obj5=Image.open("images/sdg/5.JPG")
obj6=Image.open("images/sdg/6.JPG")
obj7=Image.open("images/sdg/7.JPG")
obj8=Image.open("images/sdg/8.JPG")
obj9=Image.open("images/sdg/9.JPG")
obj10=Image.open("images/sdg/10.JPG")
obj11=Image.open("images/sdg/11.JPG")
obj12=Image.open("images/sdg/12.JPG")
obj13=Image.open("images/sdg/13.JPG")
obj14=Image.open("images/sdg/14.JPG")
obj15=Image.open("images/sdg/15.JPG")
obj16=Image.open("images/sdg/16.JPG")
obj17=Image.open("images/sdg/17.JPG")
obj18=Image.open("images/sdg/18.JPG")


#La siguiente función se utiliza para extrer el número de sdgs de un proyecto
def extraer_numeros(cadena):
    # Utilizar expresión regular para encontrar todos los números en la cadena
    numeros = re.findall(r'\b\d+\b', cadena)
    
    # Convertir los números de texto a variables numéricas (int o float)
    numeros_numericos = [int(num) if num.isdigit() else float(num) for num in numeros]
    
    return numeros_numericos

# Ejemplo de uso
cadena_texto = sdgs_table
numeros_encontrados = extraer_numeros(cadena_texto)

tamaño_letra = 50
titulo_html = f"<h1 style='text-align: center; color: #096418; font-size: {tamaño_letra}px;'>This project focuses on these sustainable sevelopment goals: {numeros_encontrados[0]}, {numeros_encontrados[1]}</h1>"
st.markdown(titulo_html, unsafe_allow_html=True)

with col1:
    st.image(obj1)
    st.image(obj2)
    st.image(obj3)

with col2:
    st.image(obj4)
    st.image(obj5)
    st.image(obj6)

with col3:
    st.image(obj7)
    st.image(obj8)
    st.image(obj9)
    
with col4:
    st.image(obj10)
    st.image(obj11)
    st.image(obj12)

with col5:
    st.image(obj13)
    st.image(obj14)
    st.image(obj15)

with col6:
    st.image(obj16)
    st.image(obj17)
    st.image(obj18)




