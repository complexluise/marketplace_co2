import streamlit as st

st.set_page_config(
    page_title="Projects Detail",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

import pandas as pd
from PIL import Image
import webbrowser
from utils.extract_from_sheets import (
    get_projects,
    get_co2_credits_generated_by_project,
    get_co2_credits_orders,
)
from geopy.geocoders import Nominatim
import pycountry
import re

from utils.components import format_as_title
from utils.models import Proyects, CO2CreditsByProject


# Oculta SideBar
st.markdown(
    """
<style>
   [data-testid="collapsedControl"] {
       display: none
   }
</style>
""",
    unsafe_allow_html=True,
)

# Oculta Footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Hide Space
st.markdown(
    """
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

### TODO
# 1. Organizar por funciones cada una de las secciones
# 2.

# Lectura tercer dataframe
df_proyectos = get_projects()
df_proyectos = df_proyectos.iloc[:-1]


# Convertir a mayusculas para el titulo
def convertir_a_mayusculas(cadena):
    return cadena.upper()


def mostrar_imagenes_por_columna(vector):
    # Interfaz de usuario

    # Crear columnas según la longitud del vector
    columns = st.columns(len(vector))

    # Mostrar imágenes en cada columna
    for i, col in enumerate(columns):
        imagen_numero = vector[i]
        col.image(f"images/sdg/{imagen_numero}.JPG", use_column_width=True)


def extraer_numeros(cadena):
    # Utilizar expresión regular para encontrar todos los números en la cadena
    numeros = re.findall(r"\b\d+\b", cadena)

    # Convertir los números de texto a variables numéricas (int o float)
    numeros_numericos = [int(num) if num.isdigit() else float(num) for num in numeros]

    return numeros_numericos


# Selectbox para elegir el proyecto a consultar
with st.spinner("Please wait"):
    opcion_elegida = st.selectbox(
        "Select the project to consulting:", df_proyectos[Proyects.PROJECT_NAME.value]
    )

    Titulo_proy = convertir_a_mayusculas(opcion_elegida)
    Color_verdeoscuro = "{Color_verdeoscuro}"

    format_as_title("NETZEO2")
    format_as_title(Titulo_proy)

# Obtiene los datos del proyecto
fila_seleccionada = df_proyectos.loc[
    df_proyectos[Proyects.PROJECT_NAME.value] == opcion_elegida, Proyects.INDUSTRY.value
].iloc[0]
Description = df_proyectos.loc[
    df_proyectos[Proyects.PROJECT_NAME.value] == opcion_elegida,
    Proyects.DESCRIPTION.value,
].iloc[0]
En = df_proyectos.loc[
    df_proyectos[Proyects.PROJECT_NAME.value] == opcion_elegida,
    Proyects.SERIAL_HEADER.value,
].iloc[0]
Location = df_proyectos.loc[
    df_proyectos[Proyects.PROJECT_NAME.value] == opcion_elegida, Proyects.LOCATION.value
].iloc[0]
sdgs_table = df_proyectos.loc[
    df_proyectos[Proyects.PROJECT_NAME.value] == opcion_elegida,
    Proyects.SUSTAINABLE_DEVELOPMENT_GOAL.value,
].iloc[0]


# Función para convertir coordenadas en texto a una tuple (,)
def convertir_a_tupla(coordenadas_str):
    """Convierte la cadena str de location a valores numericos"""
    try:
        latitud, longitud = map(float, coordenadas_str.split(","))
        return (latitud, longitud)
    except ValueError:
        return None


# Conversión de textp a tupla
input_text = Location
coordinates_transformed = convertir_a_tupla(input_text)


# Funciones para obtener información de las coordenadas
geolocator = Nominatim(user_agent="app")
location = geolocator.reverse(coordinates_transformed)

try:
    # Intenta acceder a la información en location
    country_code = location.raw["address"]["country_code"]
    country_name = pycountry.countries.get(alpha_2=country_code).name
    # Resto del código que utiliza country_code
except (AttributeError, KeyError):
    # Manejo de la excepción si hay un error al acceder a location.raw
    country_code = None  # Otra opción es asignar un valor por defecto o hacer algo diferente según tus necesidades
    country_name = None


# Dividir la pantalla en cuatro columnas
col1, col2, col3, col4 = st.columns(4)

# Obtemción de información del google sheets+
df_bonos_proyecto = get_co2_credits_generated_by_project()
df_ordenes_compra = get_co2_credits_orders()


# Metodologia y bonos generados
Metodologias = df_bonos_proyecto.loc[
    df_bonos_proyecto[Proyects.PROJECT_NAME.value] == opcion_elegida,
    CO2CreditsByProject.METHODOLOGY.value,
].iloc[0]
bonos_generados = df_bonos_proyecto.loc[
    df_bonos_proyecto[Proyects.PROJECT_NAME.value] == opcion_elegida,
    CO2CreditsByProject.CREDITS_GENERATED.value,
].iloc[0]


with col1:
    image5 = Image.open("images/obj/f5.JPG")  # Imagen de la ubicación
    image5 = image5.resize((800, 600))
    with st.columns(3)[1]:
        st.image(image5)

    st.markdown(
        "<p style='text-align: center;'><strong>Location:</strong></p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='text-align: center;'>{country_name}</p>", unsafe_allow_html=True
    )

with col2:
    image6 = Image.open("images/obj/f6.JPG")  # Imagen planta, tipo de industría
    image6 = image6.resize((800, 600))
    with st.columns(3)[1]:
        st.image(image6)
    st.markdown(
        "<p style='text-align: center;'><strong>Industry:</strong></p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='text-align: center;'>{fila_seleccionada}</p>",
        unsafe_allow_html=True,
    )

with col3:
    image7 = Image.open("images/obj/f7.JPG")  # Imagen metodología
    image7 = image7.resize((800, 600))
    with st.columns(3)[1]:
        st.image(image7)
    st.markdown(
        "<p style='text-align: center;'><strong>Methodology:</strong></p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='text-align: center;'>{Metodologias}</p>", unsafe_allow_html=True
    )


with col4:
    image8 = Image.open("images/obj/f8.JPG")  # Imagen creditos, carro de compra
    image8 = image8.resize((800, 600))
    with st.columns(3)[1]:
        st.image(image8)
    st.markdown(
        "<p style='text-align: center;'><strong>Generated CO2 credits:</strong></p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='text-align: center;'>{int(bonos_generados)}</p>",
        unsafe_allow_html=True,
    )


image9 = Image.open("images/obj/f9.JPG")  # Imagen de turbinas eloicas


image9 = image9.resize((1250, 480))
st.image(image9)

st.divider()

col1, col2 = st.columns(2)


# Función para generar barra con dos cadenas de texto
def barra(a, b):
    st.info(f"**{a}**: {b}")


with col1:
    tamaño_letra = 40
    format_as_title("About")

    st.write("Description of projects: ", Description)

    # Funciones para la app
    geolocator = Nominatim(user_agent="app")
    location = geolocator.reverse(coordinates_transformed)
    # Variable vacia
    Empty = ""
    if country_code != Empty:
        country_code = location.raw["address"]["country_code"]
        country_name = pycountry.countries.get(alpha_2=country_code).name
    else:
        location = coordinates_transformed
        country_name = coordinates_transformed

    # if opcion_elegida != "Parque Eólico Costa Azul":
    # TODO Esto deberia ser más general porque pueden existir proyectos diferentes a Costa Azul que cumplen esta misma condición
    #   geolocator = Nominatim(user_agent="app")
    #   location = geolocator.reverse(coordinates_transformed)
    #   country_code = location.raw["address"]["country_code"]
    #    country_name = pycountry.countries.get(alpha_2=country_code).name
    #  else:
    #    location = coordinates_transformed
    #    country_name = coordinates_transformed

    coo = "Coordinates"
    Pais = "Country"

    Proyecto = Proyects.PROJECT_NAME.value
    barra(Proyecto, opcion_elegida)

    if country_code != Empty:
        Localizacion_proyecto = "Location Project"
        barra(Localizacion_proyecto, country_name)

    Industria_tipo = "Industry Type"
    barra(Industria_tipo, fila_seleccionada)

    sdg_proyecto = "List SDG"
    barra(sdg_proyecto, sdgs_table)


# Agregar contenido a la segunda columna
with col2:
    tamaño_letra = 40
    Titulo_mapa = f"<h1 style='text-align: center; color: #576F57; font-size: {tamaño_letra}px;'>Mapa of {country_name}</h1>"
    st.markdown(Titulo_mapa, unsafe_allow_html=True)

    ct_coordinates = coordinates_transformed

    # Crear un DataFrame con las coordenadas de Bogotá
    data = {"LATITUDE": [ct_coordinates[0]], "LONGITUDE": [ct_coordinates[1]]}
    df = pd.DataFrame(data)

    # Mostrar el mapa en Streamlit con st.map()
    st.map(df, zoom=11)

st.divider()

tamaño_letra = 50
Mas_informacion = f"<h1 style='text-align: center; color: #576F57; font-size: {tamaño_letra}px;'>More information</h1>"
st.markdown(Mas_informacion, unsafe_allow_html=True)

prov = df_bonos_proyecto.loc[
    df_bonos_proyecto[Proyects.PROJECT_NAME.value] == opcion_elegida,
    CO2CreditsByProject.PROVIDER.value,
].iloc[0]
entity = df_bonos_proyecto.loc[
    df_bonos_proyecto[Proyects.PROJECT_NAME.value] == opcion_elegida,
    CO2CreditsByProject.VERIFYING_ENTITY.value,
].iloc[0]
g_b = df_bonos_proyecto.loc[
    df_bonos_proyecto[Proyects.PROJECT_NAME.value] == opcion_elegida,
    CO2CreditsByProject.CREDITS_GENERATED.value,
].iloc[0]
b_p = df_bonos_proyecto.loc[
    df_bonos_proyecto[Proyects.PROJECT_NAME.value] == opcion_elegida,
    CO2CreditsByProject.BUNDLED_CO2_CREDITS.value,
].iloc[0]
b_d = df_bonos_proyecto.loc[
    df_bonos_proyecto[Proyects.PROJECT_NAME.value] == opcion_elegida,
    CO2CreditsByProject.AVAILABLE_CO2_CREDITS.value,
].iloc[0]
n_s = df_bonos_proyecto.loc[
    df_bonos_proyecto[Proyects.PROJECT_NAME.value] == opcion_elegida,
    CO2CreditsByProject.SERIAL_NUMBER_CO2_CREDITS.value,
].iloc[0]
stt = df_bonos_proyecto.loc[
    df_bonos_proyecto[Proyects.PROJECT_NAME.value] == opcion_elegida,
    CO2CreditsByProject.STATUS_BUNDLED.value,
].iloc[0]

Localizacion_proyecto = CO2CreditsByProject.PROVIDER.value
barra(Localizacion_proyecto, country_name)

Industria_tipo = "Verification Entity"  # TODO
barra(Industria_tipo, entity)

sdg_proyecto = CO2CreditsByProject.METHODOLOGY.value
barra(sdg_proyecto, Metodologias)

generated_bones = "Generated CO2 Credits"  # TODO
barra(generated_bones, int(g_b))

bones_pk = "CO2 Credits in a Package"  # TODO
barra(bones_pk, int(b_p))

available = "Available CO2 Credits"  # TODO
barra(available, int(b_d))

ser = "Serial Number"  # TODO
barra(ser, n_s)

status_type = CO2CreditsByProject.STATUS_BUNDLED.value
barra(status_type, stt)

st.divider()

# Ejemplo de uso
cadena_texto = sdgs_table
numeros_encontrados = extraer_numeros(cadena_texto)

tamaño_letra = 50
titulo_html = f"<h1 style='text-align: center; color: #576F57; font-size: {tamaño_letra}px;'>This project focuses on these sustainable development goals:</h1>"
st.markdown(titulo_html, unsafe_allow_html=True)

mostrar_imagenes_por_columna(numeros_encontrados)


title_sdg = convertir_a_mayusculas("Sustainable development goals")

st.markdown(
    f"<h1 style='text-align: center; color: #576F57;'>{title_sdg}</h1>",
    unsafe_allow_html=True,
)

TextSDG = """
    <div style='text-align: center; font-size: 24px;'>
        <p style='text-align: justify;'>
            The 2030 Agenda for Sustainable Development, adopted by all United Nations Member States in 2015, provides a shared blueprint for peace and prosperity for people and the planet, now and into the future. At its heart are the 17 Sustainable Development Goals (SDGs), which are an urgent call for action by all countries - developed and developing - in a global partnership. They recognize that ending poverty and other deprivations must go hand-in-hand with strategies that improve health and education, reduce inequality, and spur economic growth – all while tackling climate change and working to preserve our oceans and forests.
        </p>
    </div>
"""
st.markdown(TextSDG, unsafe_allow_html=True)

url = "https://sdgs.un.org/goals"
if st.button("Learn more about the Sustainable Development Goals."):
    webbrowser.open_new_tab(url)
