import pytest
from utils.extract_from_sheets import (
    select_columns,
    filter_rows_with_data,
    get_projects,
    conn,
)
from pandas import DataFrame
from pandas.testing import assert_frame_equal
from unittest.mock import MagicMock

# Mock DataFrame to be returned by conn.read
mock_df_projects = DataFrame(
    {
        "Project Name": ["Project A", "Project B", "Project C"],
        "Industry": ["Tech", "Health", "Finance"],
        "Serial Header": ["001", "002", "003"],
        "Sustainable Development Goal": ["Goal 1", "Goal 2", "Goal 3"],
        "Other Column": [10, 20, 30],
    }
)

# Mock DataFrame for Bonos_Proyecto
mock_df_bonos_project = DataFrame(
    {
        "Project Name": ["Project X", "Project Y"],
        "Number of Credits Generated": [100, 200],
        "Status": ["Active", "Inactive"],
        # ... other columns
    }
)

# Mock DataFrame for Ordenes_Bonos
mock_df_bonos_purchased = DataFrame(
    {
        "Buyer's Name": ["Alice", "Bob"],
        "Purchase Order": [123, 456],
        "Bonds Purchased": [10, 20],
        "Status": ["Completed", "Pending"],
        # ... other columns
    }
)


@pytest.fixture
def mock_conn_read(mocker):
    # Mock conn.read to return the appropriate DataFrame based on the worksheet name
    def mock_read(worksheet, ttl, nrows):
        if worksheet == "Bonos_Proyecto":
            return mock_df_bonos_project
        if worksheet == "Proyectos":
            return mock_df_projects
        elif worksheet == "Ordenes_Bonos":
            return mock_df_bonos_purchased

    mocker.patch.object(conn, "read", side_effect=mock_read)


def test_get_projects(mock_conn_read):
    # Call the function
    result_df = get_projects()

    # Expected DataFrame after processing
    expected_df = DataFrame(
        {
            "Project Name": ["Project A", "Project B", "Project C"],
            "Industry": ["Tech", "Health", "Finance"],
            "Serial Header": ["001", "002", "003"],
            "Sustainable Development Goal": ["Goal 1", "Goal 2", "Goal 3"],
        }
    )

    # Assert that the result matches the expectation
    assert_frame_equal(result_df, expected_df)


# Test for select_columns
def test_select_columns():
    # Create a mock DataFrame
    df_mock = DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})

    # Expected DataFrame
    expected_df = DataFrame({"B": [4, 5, 6], "C": [7, 8, 9]})

    result_df = select_columns(df_mock, "B", "C")
    assert_frame_equal(result_df, expected_df)


# Test for filter_rows_with_data
def test_filter_rows_with_data():
    # Create a mock DataFrame
    df_mock = DataFrame({"Name": ["Alice", "Bob", None], "Age": [30, None, 25]})

    # Expected DataFrame
    expected_df = DataFrame({"Name": ["Alice"], "Age": [30.0]})

    result_df = filter_rows_with_data(df_mock, ["Name", "Age"])
    assert_frame_equal(result_df, expected_df)