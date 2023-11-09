import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'tabla1.csv'  # Reemplaza con la ruta de tu archivo CSV
data = pd.read_csv(file_path)


Parte1 = data.head(5)
print(Parte1)
Parte1.head()