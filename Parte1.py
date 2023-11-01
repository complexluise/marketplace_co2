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
