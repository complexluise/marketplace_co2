import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'tabla3.csv'  # Reemplaza con la ruta de tu archivo CSV
data = pd.read_csv(file_path)

# Manejar los valores NaN en la columna 'Industría'
data['Industría'].fillna('Desconocido', inplace=True)

categorias = data['Industría'].unique().tolist()

print(categorias)

# Obtener las frecuencias de cada nombre
frecuencias = data['Industría'].value_counts()

# Crear un vector con las frecuencias en el mismo orden que categorias
ventas = [frecuencias[i] for i in categorias]
porcentajes = [i/np.sum(ventas) for i in ventas]
print(porcentajes)
