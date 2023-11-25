import streamlit as st
from utils.extract_from_sheets import get_co2_credits_generated_by_project

from utils.components import format_as_title


st.set_page_config(
    page_title="Marketplace Proyects",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)

format_as_title("Market Place Projects")

format_as_title("Table of CO2 Credits Purchases by Project")

with st.spinner("Please wait"):
    df = get_co2_credits_generated_by_project()
    st.dataframe(df)
