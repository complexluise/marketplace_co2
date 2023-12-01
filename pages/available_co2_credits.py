import streamlit as st
import plotly.express as px
from utils.components import format_as_title
from utils.extract_from_sheets import get_industry_data
from utils.models import Proyects, CO2CreditsByProject

st.set_page_config(
    page_title="Available Bonds",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)

with st.spinner("Please wait"):
    format_as_title("Available CO2 Credits")
    df = get_industry_data()
    fig = px.pie(
        df,
        values=CO2CreditsByProject.CREDITS_GENERATED.value,
        names=Proyects.INDUSTRY.value,
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )

    st.plotly_chart(fig, use_container_width=True)


def main():
    pass
