import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(
    page_title="Projects Detail",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

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

from utils.extract_from_sheets import get_co2_credits_generated_by_project
from utils.models import CO2CreditsByProject

df = get_co2_credits_generated_by_project()
column_config_co2_credits_by_project = {
    CO2CreditsByProject.PROJECT_NAME.value: st.column_config.Column(
        "Project",
        # width="small",
    ),
    CO2CreditsByProject.AVAILABLE_CO2_CREDITS.value: st.column_config.Column(
        "Available CO2 Credits",  # width="small"
    ),
    CO2CreditsByProject.SERIAL_NUMBER_CO2_CREDITS.value: st.column_config.Column(
        "Serial Number CO2 Credits",  # width="small"
    ),
    CO2CreditsByProject.STATUS_BUNDLED.value: st.column_config.Column(
        "Status Bundled CO2 Credits",  # width="small"
    ),
}

st.write("# Tablas por defecto de Streamlit")

st.dataframe(
    data=df[column_config_co2_credits_by_project.keys()],
    use_container_width=True,
    hide_index=True,
    column_config=column_config_co2_credits_by_project,
)

st.write("# Tablas sencillas")

hide_streamlit_style = """
            <style>
            tbody th {display:none}
            .blank{
            display: none;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.table(data=df[column_config_co2_credits_by_project.keys()].style.hide(axis="index"))

st.write("# Tablas con aggrid")

gb = GridOptionsBuilder.from_dataframe(df[column_config_co2_credits_by_project.keys()])

gb.configure_default_column(editable=True)
grid_options = gb.build()

st.write("## Tema Streamlit")
AgGrid(
    df[column_config_co2_credits_by_project.keys()],
    theme="streamlit",
    key="table1",
    gridOptions=grid_options,
    allow_unsafe_jscode=True,
    fit_columns_on_grid_load=True,
    reload_data=False,
    try_to_convert_back_to_original_types=False,
)

st.write("## Tema Material")
AgGrid(
    df[column_config_co2_credits_by_project.keys()],
    theme="material",
    key="table2",
    gridOptions=grid_options,
    allow_unsafe_jscode=True,
    fit_columns_on_grid_load=True,
    reload_data=False,
    try_to_convert_back_to_original_types=False,
)
