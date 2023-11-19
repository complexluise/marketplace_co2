import streamlit as st

from utils.extract_from_sheets import get_bonos_purchased

df = get_bonos_purchased()

st.dataframe(df)
