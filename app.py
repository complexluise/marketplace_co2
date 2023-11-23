import streamlit as st

from utils.extract_from_sheets import get_co2_credits_orders

df = get_co2_credits_orders()

st.dataframe(df)
