from typing import List

from streamlit import connection

from pandas import DataFrame, merge
from streamlit_gsheets import GSheetsConnection

from utils.models import (
    Proyects,
    CO2CreditsByProject,
    CO2CreditsByOrders,
    SheetsDatabase,
)


# Create a connection object.
conn = connection("gsheets", type=GSheetsConnection)


def select_columns(df: DataFrame, column_start: str, column_end: str) -> DataFrame:
    """
    Selects a range of columns from the DataFrame based on column names.

    Args:
        df (DataFrame): The DataFrame from which to select columns.
        column_start (str): The name of the starting column.
        column_end (str): The name of the ending column.

    Returns:
        DataFrame: A new DataFrame containing columns from column_start to column_end.
    """
    return df.loc[:, column_start:column_end]


def filter_rows_with_data(df: DataFrame, columnas_requeridas: List[str]) -> DataFrame:
    """
    Filters rows in the DataFrame that have non-NA values for all specified columns.

    Args:
        df (DataFrame): The DataFrame to filter.
        columnas_requeridas (List[str]): List of column names to check for non-NA values.

    Returns:
        DataFrame: A DataFrame containing rows where all specified columns have non-NA values.
    """
    return df[df[columnas_requeridas].notna().all(axis=1)]


def get_projects() -> DataFrame:
    """
    Retrieves project data from a Google Sheets worksheet named 'Proyectos'. # TODO CHANGE TO PROJECTS

    Returns:
        DataFrame: A DataFrame containing selected columns and rows with data for projects.
    """
    df_projects = conn.read(
        worksheet=SheetsDatabase.PROJECTS.value,
        ttl=0,
        nrows=1000,
    )

    return df_projects.pipe(
        select_columns,
        column_start=Proyects.PROJECT_NAME.value,
        column_end=Proyects.SUSTAINABLE_DEVELOPMENT_GOAL.value,
    ).pipe(
        filter_rows_with_data,
        columnas_requeridas=[
            Proyects.PROJECT_NAME.value,
            Proyects.INDUSTRY.value,
            Proyects.SERIAL_HEADER.value,
        ],
    )


def get_co2_credits_generated_by_project() -> DataFrame:
    """
    Retrieves data from a Google Sheets worksheet named 'Bonos_Proyecto'. # TODO CHANGE TO CO2_CREDITS_PROYECTS

    Returns:
        DataFrame: A DataFrame containing selected columns and rows with data for bonos projects.
    """
    df_co2_credits_project = conn.read(
        worksheet=SheetsDatabase.PROJECTS_BONUS.value,
        ttl=0,
        nrows=1000,
    )
    return df_co2_credits_project.pipe(
        select_columns,
        column_start=CO2CreditsByProject.PROJECT_NAME.value,
        column_end=CO2CreditsByProject.STATUS.value,
    ).pipe(
        filter_rows_with_data,
        columnas_requeridas=[
            CO2CreditsByProject.PROJECT_NAME.value,
            CO2CreditsByProject.CREDITS_GENERATED.value,
        ],
    )


def get_co2_credits_orders() -> DataFrame:
    """
    Retrieves data from a Google Sheets worksheet named 'Ordenes_Bonos'. # TODO CHANGE TO CO2_CREDITS_ORDERS

    Returns:
        DataFrame: A DataFrame containing selected columns and rows with data for purchased bonos.
    """
    df_co2_credits_orders = conn.read(
        worksheet=SheetsDatabase.ORDER_BONUS.value,
        ttl=0,
        nrows=1000,
    )
    return df_co2_credits_orders.pipe(
        select_columns,
        column_start=CO2CreditsByOrders.BUYERS_NAME.value,
        column_end=CO2CreditsByOrders.COMPENSATION_DESCRIPTION.value,
    ).pipe(
        filter_rows_with_data,
        columnas_requeridas=[
            CO2CreditsByOrders.BUYERS_NAME.value,
            CO2CreditsByOrders.PURCHASE_ORDER.value,
            CO2CreditsByOrders.BONDS_PURCHASED.value,
            CO2CreditsByOrders.STATUS.value,
        ],
    )


def get_co2_credits_project_enriched() -> DataFrame:
    """
    Enriches bonos project data by merging it with the projects data.

    Returns:
        DataFrame: A merged DataFrame containing enriched data for bonos projects.
    """
    df_projects = get_projects()
    df_co2_credits_project = get_co2_credits_generated_by_project()

    return merge(df_co2_credits_project, df_projects, how="inner")


def get_industry_data() -> DataFrame:
    df_co2_credits_project_enriched = get_co2_credits_project_enriched()
    df_pivot_industry = df_co2_credits_project_enriched.groupby(
        by=Proyects.INDUSTRY.value
    ).sum()
    df_pivot_industry.reset_index(inplace=True)
    return df_pivot_industry


if __name__ == "__main__":
    df = get_co2_credits_project_enriched()
