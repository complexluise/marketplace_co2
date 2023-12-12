import plotly.graph_objs as go
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode

from utils.components import format_as_title
from utils.extract_from_sheets import (
    get_co2_credits_generated_by_project,
    get_co2_credits_orders,
)

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


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

format_as_title("Market Place Projects")

format_as_title("Table of CO2 Credits Purchases by Project")

# with st.spinner("Please wait"):
#    df = get_co2_credits_generated_by_project()
#    # st.dataframe(data=df, use_container_width=True, hide_index=True)
#    fig = go.Figure(
#        data=[
#            go.Table(
#                header=dict(
#                    values=list(df.columns), fill_color="paleturquoise", align="left"
#                ),
#                cells=dict(
#                    values=[df[column] for column in df.columns],
#                    fill_color="lavender",
#                    align="left",
#                ),
#            )
#        ]
#    )
#    st.plotly_chart(fig, width=600)


format_as_title("CO2 Credits Orders")

with st.spinner("Please wait"):
    df = get_co2_credits_orders()
    st.dataframe(data=df, use_container_width=True, hide_index=True)


gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(editable=True)

response = AgGrid(
    df,
    editable=True,
    gridOptions=gb.build(),
    data_return_mode="filtered_and_sorted",
    update_mode="no_update",
    fit_columns_on_grid_load=True,
    theme="material",
    columns_auto_size_mode=ColumnsAutoSizeMode.FIT_ALL_COLUMNS_TO_VIEW,
)
