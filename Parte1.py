import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Título de la página
st.title('Información sobre Bonos de Carbono')

# Texto sobre bonos de carbono
st.write("""
Los bonos de carbono son instrumentos financieros que buscan mitigar el cambio climático al incentivar la reducción de emisiones de gases de efecto invernadero. Empresas y países pueden comprar bonos de carbono para compensar sus emisiones, financiando proyectos sostenibles.
A continuación, se muestra una tabla con datos de empresas, precios de bonos, cantidad comprada y totales.
""")

import webbrowser

# Título de la página
st.title('Redirección a proyecto GitHub')

# URL a la que se redirigirá
url = 'https://github.com/complexluise/marketplace_co2/blob/main/Parte1.py'

# Botón para redirigir a la URL
if st.button('GitHub'):
    webbrowser.open_new_tab(url)

url2 = 'http://localhost:8502'

# Botón para redirigir a la URL
if st.button('LocalHost'):
    webbrowser.open_new_tab(url2)

# Datos para la tabla
data = {
    'Empresa': ['Empresa A', 'Empresa B', 'Empresa C'],
    'Precio de los Bonos': [10, 12, 9],
    'Cantidad Comprada': [100, 75, 120],
}

# Creación del DataFrame
df = pd.DataFrame(data)
df['Total'] = df['Precio de los Bonos'] * df['Cantidad Comprada']

# Mostrar la tabla
st.write(df)

st.title("¿Quién verifica la validez de los bonos de carbono del mercado? ")

st.title('Recuadros interactivos en Streamlit')

# Crear un expander
with st.expander("Información adicional 1"):
    st.write("Aquí puedes agregar más información, gráficos, tablas, etc.")

# Otro expander
with st.expander("Información adicional 2"):
    st.write("Esta es otra sección expandible para más contenido.")

st.write("Para garantizar su veracidad, los proyectos de bonos de carbono son verificados por entes internacionales que validan y certifican la reducción de emisiones a partir del proyecto y sus beneficios socioambientales.  Para poder certificar bajo alguna de estas entidades, la empresa que emite estos bonos de carbono se adhiere a un estricto conjunto de estándares. Una vez que la empresa atravesó todo el proceso de verificación, se le otorga una certificación y el logo de la entidad reguladora.  Esta certificación brinda a los compradores la seguridad de que la empresa que emite los bonos se ha sometido a procesos de auditoría que garantizan la trazabilidad de todos sus procesos. ")

# Datos para el gráfico de torta
categorias = ['Empresa 1', 'Empresa 2', 'Empresa 3', 'Empresa 4']
ventas = [300, 450, 200, 350]

# Creación del gráfico de torta con Matplotlib
fig, ax = plt.subplots()
ax.pie(ventas, labels=categorias, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Aspecto de círculo

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

st.title("UBICACIONES ")
st.write("Las empresas pueden acceder a la compra de bonos de carbono para compensar las emisiones de carbono asociadas a sus procesos productivos. ")
import pandas as pd

# Título de la página
st.title('Visualización de Localización en Mapa.')

# Coordenadas de Bogotá, Colombia
bogota_lat = 4.7109886
bogota_lon = -74.072092

# Crear un DataFrame con las coordenadas de Bogotá
data = {
    'LATITUDE': [bogota_lat],
    'LONGITUDE': [bogota_lon]
}
df = pd.DataFrame(data)

# Mostrar el mapa en Streamlit con st.map()
st.map(df, zoom=11)

# Página 1 - Contenido inicial
st.title('Página 1')
st.write('Contenido de la página 1')
# Botón para ir a la página 2
if st.button('Ir a la Página 2'):
    page = 'page2'

# Página 2 - Contenido de la segunda "página"
if 'page' in locals() and page == 'page2':
    st.title('Página 2')
    st.write('¡Bienvenido a la página 2!')
    # Botón para volver a la página 1
    if st.button('Volver a la Página 1'):
        page = 'page1'



import streamlit as st
from pagina1 import main as pagina1_main
from pagina2 import main as pagina2_main

page = st.experimental_get_query_params().get("page", 1)

if page == 1:
    pagina1_main()
elif page == 2:
    pagina2_main()

st.title("Okey, aqui pondremos el siguiente ejemplo de como hacer esta pagina")

import streamlit as st

# Opción para seleccionar la página
pagina = st.radio("Selecciona una página", ["Página 1", "Página 2"])

if pagina == "Página 1":
    st.title("Contenido de la Página 1")
    st.write("Este es el contenido de la Página 1")

elif pagina == "Página 2":
    st.title("Contenido de la Página 2")
    st.write("Este es el contenido de la Página 2")

st.title("VAAAAMOS A CREAAAR TODA LA PAGINA WEB BIEN CHEVERE")

def pagina1():
    st.title('Página 1')
    st.write('Este es el contenido de la Página 1')

def pagina2():
    st.title('Página 2')
    st.write('Este es el contenido de la Página 2')

def main():
    menu = st.sidebar.radio("Menú", ("Página 1", "Página 2"))

    if menu == "Página 1":
        pagina1()
    elif menu == "Página 2":
        pagina2()

if __name__ == '__main__':
    main()