from typing import List

from streamlit import connection

from pandas import DataFrame, merge
from streamlit_gsheets import GSheetsConnection

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
    Retrieves project data from a Google Sheets worksheet named 'Proyectos'.

    Returns:
        DataFrame: A DataFrame containing selected columns and rows with data for projects.
    """
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


def get_bonos_project() -> DataFrame:
    """
    Retrieves data from a Google Sheets worksheet named 'Bonos_Proyecto'.

    Returns:
        DataFrame: A DataFrame containing selected columns and rows with data for bonos projects.
    """
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


def get_bonos_purchased() -> DataFrame:
    """
    Retrieves data from a Google Sheets worksheet named 'Ordenes_Bonos'.

    Returns:
        DataFrame: A DataFrame containing selected columns and rows with data for purchased bonos.
    """
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


def get_bonos_project_enriched() -> DataFrame:
    """
    Enriches bonos project data by merging it with the projects data.

    Returns:
        DataFrame: A merged DataFrame containing enriched data for bonos projects.
    """
    df_projects = get_projects()
    df_bonos_project = get_bonos_project()

    return merge(df_bonos_project, df_projects, how="inner")

if __name__ == '__main__':
    df = get_bonos_project_enriched()
