import streamlit as st
from utils.extract_from_sheets import get_co2_credits_generated_by_project

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

st.write("Market Place Projects")

st.write("Table of CO2 Credits Purchases by Project")

df = get_co2_credits_generated_by_project()


# st.dataframe(get_co2_credits_project_enriched())
