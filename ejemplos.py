import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df3 = pd.read_csv('tabla3.csv')  # Reemplaza con la ruta de tu archivo CSV
df3 = df3.iloc[:-1]
#df3.head()
#print(df3)


# Crear un recuadro para seleccionar una opción
opcion_elegida = st.selectbox("Selecciona una opción:", df3["Nombre de proyecto"])


# Obtener el valor en la columna 'Nombre' para la misma fila
valor_nombre = df3.loc[df3['Nombre de proyecto'] == opcion_elegida, 'Industría'].iloc[0]
# valor_otra_columna = fila_seleccionada['SDG '].iloc[0]
# Mostrar el resultado en la página web
Location = df3.loc[df3['Nombre de proyecto'] == opcion_elegida, 'Ubicacion '].iloc[0]

def convertir_a_tupla(coordenadas_str):
    try:
        latitud, longitud = map(float, coordenadas_str.split(','))
        return (latitud, longitud)
    except ValueError:
        return None

print("xd",Location, type(Location), convertir_a_tupla(Location), type(convertir_a_tupla(Location)), type((40.7128, -74.0060)))