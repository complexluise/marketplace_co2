from typing import List

import streamlit as st

from pandas import DataFrame
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)


def select_columns(df: DataFrame, column_start: str, column_end: str) -> DataFrame:
    return df.loc[:, column_start:column_end]


def filter_rows_with_data(df: DataFrame, columnas_requeridas: List[str]) -> DataFrame:
    return df[df[columnas_requeridas].notna().all(axis=1)]


def get_projects() -> DataFrame:
    df_projects = conn.read(
        worksheet="Proyectos",
        ttl=0,
        nrows=1000,
    )

    return df_projects.pipe(
        select_columns,
        column_start="Project Name",
        column_end="Sustainable Development Goal",
    ).pipe(
        filter_rows_with_data,
        columnas_requeridas=[
            "Project Name",
            "Industry",
            "Serial Header",
        ],
    )


def get_bonos_project():
    df_bonos_project = conn.read(
        worksheet="Bonos_Proyecto",
        ttl=0,
        nrows=1000,
    )
    return df_bonos_project.pipe(
        select_columns,
        column_start="Project Name",
        column_end="Status",
    ).pipe(
        filter_rows_with_data,
        columnas_requeridas=["Project Name", "Number of Credits Generated"],
    )


def get_bonos_purchased():
    df_bonos_purchased = conn.read(
        worksheet="Ordenes_Bonos",
        ttl=0,
        nrows=1000,
    )
    return df_bonos_purchased.pipe(
        select_columns,
        column_start="Buyer's Name",
        column_end="Compensation Description",
    ).pipe(
        filter_rows_with_data,
        columnas_requeridas=[
            "Buyer's Name",
            "Purchase Order",
            "Bonds Purchased",
            "Status",
        ],
    )
