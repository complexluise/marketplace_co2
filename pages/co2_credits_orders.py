import streamlit as st

from utils.components import format_as_title
from utils.extract_from_sheets import get_co2_credits_orders

st.set_page_config(
    page_title="CO2 Credits Orders",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)

format_as_title("Ordenes de Bonos")

with st.spinner("Please wait"):
    df = get_co2_credits_orders()
    st.dataframe(df)
