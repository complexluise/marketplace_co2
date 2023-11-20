from utils.extract_from_sheets import get_projects
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64
import numpy as np
from PIL import Image
import webbrowser

df = get_projects()
nombres_columnas = df.columns[0]

# Imprimir los nombres de las columnas
print("Nombres de las columnas:", nombres_columnas)

#st.title("Net Zeo 2")
#st.title("COSTA AZUL WIND PARK")
st.header(nombres_columnas)