import pytest
from datetime import datetime, date
from src.date_difference import calculate_days_between_dates

def test_calculate_days_between_dates_string_input():
    """Test calculating days between dates using string inputs"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9
    assert calculate_days_between_dates('2023-01-10', '2023-01-01') == 9

def test_calculate_days_between_dates_datetime_input():
    """Test calculating days between dates using datetime inputs"""
    date1 = datetime(2023, 1, 1)
    date2 = datetime(2023, 1, 10)
    assert calculate_days_between_dates(date1, date2) == 9
    assert calculate_days_between_dates(date2, date1) == 9

def test_calculate_days_between_dates_date_input():
    """Test calculating days between dates using date inputs"""
    date1 = date(2023, 1, 1)
    date2 = date(2023, 1, 10)
    assert calculate_days_between_dates(date1, date2) == 9
    assert calculate_days_between_dates(date2, date1) == 9

def test_calculate_days_between_dates_same_date():
    """Test calculating days between the same date"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_calculate_days_between_dates_different_years():
    """Test calculating days between dates in different years"""
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1

def test_invalid_date_format():
    """Test handling of invalid date formats"""
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates('2023/01/01', '2023-01-10')
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates('2023-1-1', '2023-01-10')

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        calculate_days_between_dates(123, '2023-01-10')
    with pytest.raises(TypeError):
        calculate_days_between_dates('2023-01-10', [1, 2, 3])