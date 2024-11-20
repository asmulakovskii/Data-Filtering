import pytest
from filter_report import display_data, apply_filters

def test_apply_filters():
    data = [{'Age': '25', 'Country': 'USA'}, {'Age': '30', 'Country': 'Canada'}, {'Age': '35', 'Country': 'USA'}]
    filters = ['Age=25-30']
    expected = [{'Age': '25', 'Country': 'USA'}, {'Age': '30', 'Country': 'Canada'}]
    assert apply_filters(data, filters) == expected

def test_display_data(capsys):
    data = [{'Age': '25', 'Country': 'USA'}, {'Age': '30', 'Country': 'Canada'}]
    display_data(data)
    captured = capsys.readouterr()
    expected_output = 'Age, Country\n25, USA\n30, Canada\n'
    assert captured.out == expected_output

def test_display_no_data(capsys):
    data = []
    display_data(data)
    captured = capsys.readouterr()
    assert captured.out == "No data matches the filter criteria.\n"

