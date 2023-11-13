import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
import numpy as np
from PIL import Image
import webbrowser

st.title("MARKETPLACE")

image1 = Image.open('Images/f1.JPG')
st.image(image1, caption='CARBON CREDITS: $18.00')



image2 = Image.open('Images/f2.JPG')
st.image(image2, caption='CARBON REMOVAL GIFT CARD: from $25.00')

st.title("MARKETPLACE PROJECTS")

st.write("In this space, we present a wide variety of projects designed to reduce carbon emissions and contribute to a cleaner and more sustainable planet. Each project in our Marketplace has been carefully selected for its positive impact on the environment and its ability to offset carbon emissions.")

image3 = Image.open('Images/f3.JPG')
st.image(image3, caption='CARBON CREDITS: $18.00')

st.title("CO2 Tons Reduced")
st.write("Explore our options and discover how you can be part of the change. By participating in these projects, you are taking concrete steps to offset your carbon footprint and help protect our precious planet.")

st.title('Graphs')
# Botón para ir a la página 2

if st.button('Graph 1'):
    page = 'page2'

if st.button('Graph 2'):
    page = 'page3'

# Código para generar los datos del diagrama de tortas
from io import BytesIO
# Importamos el df tabla3.csv
df = pd.DataFrame("tabla3.csv")

# Contar la frecuencia de cada categoría en la columna 'Industria'
conteo_categorias = df['Industría'].value_counts()
fig2, ax = plt.subplots(figsize=(8, 8))
ax.pie(conteo_categorias, labels=conteo_categorias.index, autopct='%1.1f%%', startangle=90)
ax.set_title('Diagrama de Torta - Distribución por Industria')

# Convertir la figura a bytes para mostrarla en Streamlit
image_stream = BytesIO()
fig2.savefig(image_stream, format='png')


# Mostrar el diagrama de torta en la página de Streamlit
st.image(image_stream.getvalue(), use_column_width=True)
st.pyplot(fig2)

# Página 2 - Contenido de la segunda "página"
if 'page' in locals() and page == 'page2':
    # TODO: Remplazar por datos de tabla3.csv 
    categorias = ['Empresa 1', 'Empresa 2', 'Empresa 3', 'Empresa 4']
    ventas = [300, 450, 200, 350]

# Creación del gráfico de torta con Matplotlib
    fig, ax = plt.subplots()
    ax.pie(ventas, labels=categorias, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Aspecto de círculo

# Mostrar el gráfico en Streamlit
    st.pyplot(fig)

    # Botón para volver a la página 1
    if st.button('Ocultar'):
        page = 'page1'

if 'page' in locals() and page == 'page3':

    anios = np.arange(2000, 2023)
    ingresos = np.random.randint(100, 1000, size=len(anios))

# Crear y mostrar la gráfica usando Matplotlib
    st.set_option('deprecation.showPyplotGlobalUse', False)  # Para evitar un warning
    fig, ax = plt.subplots()
    ax.plot(anios, ingresos, marker='o')

# Configuración del gráfico
    ax.set(xlabel='Año', ylabel='Ingresos en Millones de Dólares',
       title='Ingresos en función del Año')
    ax.grid()

# Mostrar la gráfica en Streamlit
    st.pyplot(fig)

    if st.button('Ocultar'):
        page = 'page1'

st.title("Current availability of carbon credits by industry.")

st.write("At NETZEO2, we continuously update our current carbon credit availability, categorized by industry. This is essential for mitigating greenhouse gas emissions and combating climate change. This assessment allows us to understand the contributions of various industries to environmental sustainability and, at the same time, identify opportunities for improvement. This analysis plays a crucial role in our commitment to a greener and more environmentally friendly economy.")

st.title("Historical supply and demand in the Netzeo2 marketplace")

st.header("Sold")
st.write("Bonds that have been verified, assigned to suppliers, and are ready for sale.")

st.header("Reserved")
st.write("Issued bonds that are held back from sale by suppliers.")

st.header("Projects")
st.write("A data set that describes carbon removal practices, such as historical and regenerative farming practices, used to calculate the total number of Bonds in a project.")

image4 = Image.open('Images/f4.JPG')
st.image(image4)

st.header("¿How to Reduce My Carbon Footprint?")
st.write("At Netzeo2, we offer solutions to help you reduce your carbon footprint and achieve your sustainability objectives. As a company that sells carbon bonds to offset CO2 emissions, we provide a range of options.")

url = 'https://github.com/complexluise/marketplace_co2/blob/main/Parte1.py'

# Botón para redirigir a la URL
if st.button('Buy Carbon Credits'):
    webbrowser.open_new_tab(url)

st.title("MARKETPLACE PROJECTS")
st.header("Table of Bond Purchases by Project")
st.write("Below, you will find the 'Table of Bond Purchases by Project,' which is updated in real-time to reflect any changes in the purchase order status. This table provides detailed information about bond purchases associated with specific projects.")

# Leer el archivo CSV
file_path = 'tabla1.csv'  # Reemplaza con la ruta de tu archivo CSV
data = pd.read_csv(file_path)
data = data.head(6)

st.write(data)

st.header("Bond Orders Table")
st.write("This table displays a detailed record of the purchased bonds, providing an insight into their traceability and current status.")

file_path = 'tabla2.csv'  # Reemplaza con la ruta de tu archivo CSV
data2 = pd.read_csv(file_path)
data2 = data2.head(6)
st.write(data2)

if st.button('Buy Carbon Credits'):
    webbrowser.open_new_tab(url)

