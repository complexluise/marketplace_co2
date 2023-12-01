from typing import List

import pandas as pd
from streamlit import connection

from pandas import DataFrame, merge
from streamlit_gsheets import GSheetsConnection

from utils.models import (
    Proyects,
    CO2CreditsByProject,
    CO2CreditsByOrders,
    SheetsDatabase,
)

# TODO debido a las limitaciones en la API de google Sheets,
#  se necesita una interfaz que permita guardar el archivo temporalmente

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


def drop_row_if_any_is_negative(df: DataFrame, column_names: list) -> DataFrame:
    """
    This function drops any rows where any of the specified columns contain a negative value.
    If the data in any of the columns are not numeric, it skips that column.

    Parameters:
    df (pandas.DataFrame): The dataframe from which rows are to be dropped.
    column_names (list): The list of column names to check for negative values.

    Returns:
    pandas.DataFrame: The dataframe with rows containing negative values in any of the specified columns dropped,
                      or the original dataframe if none of the specified columns are numeric.
    """
    # Iterate over the list of column names
    for column_name in column_names:
        # Check if the specified column exists and if the data are numeric
        if column_name in df.columns and pd.api.types.is_numeric_dtype(df[column_name]):
            # Drop rows where the specified column contains a negative value
            df: DataFrame = df[df[column_name] >= 0]

    return df


def get_projects() -> DataFrame:
    """
    Retrieves project data from a Google Sheets worksheet named 'PROJECTS'.

    Returns:
        DataFrame: A DataFrame containing selected columns and rows with data for projects.
    """
    df_projects: DataFrame = conn.read(
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
    Retrieves data from a Google Sheets worksheet named 'CO2_CREDITS_PROYECTS'.

    Returns:
        DataFrame: A DataFrame containing selected columns and rows with data for bonos projects.
    """
    df_co2_credits_project = conn.read(
        worksheet=SheetsDatabase.CO2_CREDITS_PROYECTS.value,
        ttl=0,
        nrows=1000,
    )
    return df_co2_credits_project.pipe(
        select_columns,
        column_start=CO2CreditsByProject.PROJECT_NAME.value,
        column_end=CO2CreditsByProject.STATUS_BUNDLED.value,
    ).pipe(
        filter_rows_with_data,
        columnas_requeridas=[
            CO2CreditsByProject.PROJECT_NAME.value,
            CO2CreditsByProject.CREDITS_GENERATED.value,
        ],
    )


def get_co2_credits_orders() -> DataFrame:
    """
    Retrieves data from a Google Sheets worksheet named 'CO2_CREDITS_ORDERS'.

    Returns:
        DataFrame: A DataFrame containing selected columns and rows with data for purchased bonos.
    """
    df_co2_credits_orders = conn.read(
        worksheet=SheetsDatabase.CO2_CREDITS_ORDERS.value,
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
    ).sum(CO2CreditsByProject.AVAILABLE_CO2_CREDITS.value)
    df_pivot_industry.reset_index(inplace=True)
    return df_pivot_industry


if __name__ == "__main__":
    df = get_co2_credits_project_enriched()
