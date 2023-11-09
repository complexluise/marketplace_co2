import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import webbrowser

def main():
    st.title('Página 2')

    st.title('Información sobre Bonos de Carbono')

# Texto sobre bonos de carbono
    st.write("""
    Los bonos de carbono son instrumentos financieros que buscan mitigar el cambio climático al incentivar la reducción de emisiones de gases de efecto invernadero. Empresas y países pueden comprar bonos de carbono para compensar sus emisiones, financiando proyectos sostenibles.

    A continuación, se muestra una tabla con datos de empresas, precios de bonos, cantidad comprada y totales.
    """)

    

# Título de la página
    st.title('Redirección a proyecto GitHub')

# URL a la que se redirigirá
    url = 'https://github.com/complexluise/marketplace_co2/blob/main/Parte1.py'

# Botón para redirigir a la URL
    if st.button('GitHub'):
        webbrowser.open_new_tab(url)

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

if st.button('Volver a la Página 1', key='go_to_page_1'):
        st.experimental_set_query_params(page=1)