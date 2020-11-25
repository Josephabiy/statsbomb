import pytest
from datetime import datetime
from dateutil.relativedelta import relativedelta
from src.utils import date_range_by_month
import src.my_sql


@pytest.fixture()
def sample_input_elements():
    """ Prepares sample input with start and end date """
    return {"START_DATE": "2020-01", "END_DATE": "2020-06"}


@pytest.fixture()
def sample_output_elements():
    """ Prepares sample out with complete list of dates"""
    return ["2020-01", "2020-02", "2020-03", "2020-04", "2020-05", "2020-06"]


def test_date_range_by_month(sample_input_elements, sample_output_elements):
    """ Test if date_range_by_month function successfully converts creates list of dates """
    START_DATE = sample_input_elements["START_DATE"]
    END_DATE = sample_input_elements["END_DATE"]
    date_range = date_range_by_month(START_DATE, END_DATE)

    assert date_range == sample_output_elements
