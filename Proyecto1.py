import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
import numpy as np


st.markdown(
    """
    <h1 style='color: blue; text-align: center;'>Project NETZEO2</h1>
    """,
    unsafe_allow_html=True
    )


st.markdown(
    """
    <div style='text-align: center;'>
        <p>Los bonos de carbono son instrumentos financieros que buscan mitigar el cambio climático al incentivar la reducción de emisiones de gases de efecto invernadero. Empresas y países pueden comprar bonos de carbono para compensar sus emisiones, financiando proyectos sostenibles.
        A continuación, se muestra una tabla con datos de empresas, precios de bonos, cantidad comprada y totales.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.title('Gráficas de ventas de carbono')
# Botón para ir a la página 2

if st.button('Gráfica 1'):
    page = 'page2'

if st.button('Gráfica 2'):
    page = 'page3'

# Página 2 - Contenido de la segunda "página"
if 'page' in locals() and page == 'page2':
    
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

# Leer el archivo CSV
file_path = 'tabla1.csv'  # Reemplaza con la ruta de tu archivo CSV
data = pd.read_csv(file_path)
data = data.head(6)

st.write(data)

st.title("Status types and definition")

st.write("Pre-Registration: The package of CO2 bonuses is registered on the marketplace but is not yet available for purchase. This stage typically involves verifying project details and carbon credits.")

st.write("In-Process: The CO2 bonus package is currently in the processing stage, where it might be undergoing further validation, accreditation, or preparation for sale."
         )
st.write("Under Verification: The package is undergoing a verification process to ensure the accuracy of the carbon credits and compliance with relevant standards and methodologies.")

if st.button('Tabla de información de Proyectos'):
    page = 'page4'

if 'page' in locals() and page == 'page4':
    file_path2 = 'tabla2.csv'  # Reemplaza con la ruta de tu archivo CSV
    data2 = pd.read_csv(file_path2)
    data2 = data2.head(6)
    st.write(data2)
    # Botón para volver a la página 1
    if st.button('Ocultar'):
        page = 'page1'

