import streamlit as st

# Configura la pagina
st.set_page_config(
    page_title="Marketplace NET ZEO2",
    layout="wide",
    initial_sidebar_state="collapsed",
)

import plotly.express as px
from utils.components import format_as_title, format_as_subtitle
from utils.extract_from_sheets import (
    get_industry_data,
    get_co2_credits_generated_by_project,
    get_co2_credits_orders,
)
from utils.models import Proyects, CO2CreditsByProject, CO2CreditsByOrders

# Oculta SideBar
st.markdown(
    """
<style>
   [data-testid="collapsedControl"] {
       display: none
   }
</style>
""",
    unsafe_allow_html=True,
)

# Oculta Footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Hide Space
st.markdown(
    """
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """,
    unsafe_allow_html=True,
)


# Title with custom CSS class
st.markdown(
        f"<h1 style='text-align: center; color: #576F58;'>Marketplace NET ZEO2</h1>",
        unsafe_allow_html=True,
    )

col1, col2 = st.columns(2)

# Paragraph with custom CSS class
with col1:
    format_as_subtitle("Available CO2 Credits")
    st.markdown(
        """
    <div class="paragraph">
        In this space, we present a wide variety of projects designed to reduce carbon emissions and contribute to a cleaner and more sustainable planet. Each project in our Marketplace has been carefully selected for its positive impact on the environment and its ability to offset carbon emissions.
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    df = get_industry_data()
    fig = px.pie(
        df,
        values=CO2CreditsByProject.CREDITS_GENERATED.value,
        names=Proyects.INDUSTRY.value,
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    fig.update_layout(height=300, showlegend=False)
    fig.update_traces(textposition="inside", textinfo="percent+label")

    st.plotly_chart(fig, use_container_width=True, height=300)


format_as_title("CO2 Credits by Project")
with st.spinner("Please wait"):
    df = get_co2_credits_generated_by_project()
    column_config_co2_credits_by_project = {
            CO2CreditsByProject.PROJECT_NAME.value: st.column_config.Column(
                "Project",
                #width="small",
            ),
            CO2CreditsByProject.AVAILABLE_CO2_CREDITS.value: st.column_config.Column(
                "Available CO2 Credits", #width="small"
            ),
            CO2CreditsByProject.SERIAL_NUMBER_CO2_CREDITS.value: st.column_config.Column(
                "Serial Number CO2 Credits", #width="small"
            ),
            CO2CreditsByProject.STATUS_BUNDLED.value: st.column_config.Column(
                "Status Bundled CO2 Credits",# width="small"
            ),
        }

    st.dataframe(
        data=df[column_config_co2_credits_by_project.keys()],
        use_container_width=True,
        hide_index=True,
        column_config=column_config_co2_credits_by_project
    )

format_as_title("CO2 Credits Orders")
with st.spinner("Please wait"):
    df = get_co2_credits_orders()
    column_config_co2_credits_by_orders = {
            CO2CreditsByOrders.BUYERS_NAME.value: st.column_config.Column(
                "Buyer's Name", width="small"
            ),
            CO2CreditsByOrders.PROJECT_NAME.value: st.column_config.Column(
                "Project Name", width="small"
            ),
            CO2CreditsByOrders.BONDS_PURCHASED.value: st.column_config.Column(
                "CO2 Credits Purchased", width="small"
            ),
            CO2CreditsByOrders.SERIAL_NUMBER.value: st.column_config.Column(
                "Serial Number", width="small"
            ),
            CO2CreditsByOrders.STATUS.value: st.column_config.Column(
                "Status", width="small"
            ),
        }

    st.dataframe(
        data=df[column_config_co2_credits_by_orders.keys()],
        use_container_width=True,
        hide_index=True,
        column_config=column_config_co2_credits_by_orders)
