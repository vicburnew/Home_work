from unittest.mock import mock_open, patch

import pandas
import pandas as pd

from src.reading_csv_excel import read_csv_file, read_excel_file

# Тестирование функции read_csv_file

mock_data = ("id;state;date;amount;currency_name;currency_code;from;to;description\n650703;EXECUTED;2023-09-05T11:30"
             ":32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации")


def test_read_csv_file_1(mock_csv_fixt):
    """Положительный тест на чтение csv файла"""
    with patch("builtins.open", new_callable=mock_open, read_data=mock_data) as mock_file:
        result = read_csv_file("fake.csv")
    assert result == mock_csv_fixt
    mock_file.assert_called()


def test_read_csv_file_2():
    """Отрицательный тест на открытие csv файла"""
    result = read_csv_file("./ata/")
    assert result == []


def test_read_csv_file_3():
    """Отрицательный тест на открытие csv файла"""
    with patch("builtins.open", new_callable=mock_open, read_data="") as mock_file:
        result = read_csv_file("fake.csv")
    assert result == []
    mock_file.assert_called()


# Тестирование функции read_excel_file

mock_data_df = pd.DataFrame({"id": ["650703"], "state": ["EXECUTED"], "date": ["2023-09-05T11:30:32Z"]})


def test_read_excel_file_1(mock_excel_fixt):
    """Положительный тест на чтение excel файла"""
    with patch("pandas.read_excel", read_data=mock_data_df) as mock_df:
        pandas.read_excel.return_value = mock_data_df
        result = read_excel_file("fake.csv")
    assert result == mock_excel_fixt
    mock_df.assert_called()


def test_read_excel_file_2():
    """Отрицательный тест на открытие excel файла"""
    result = read_excel_file("./ata/")
    assert result == []


def test_read_excel_file_3():
    """Отрицательный тест на открытие excel файла"""
    with patch("builtins.open", new_callable=mock_open, read_data="") as mock_file:
        result = read_excel_file("fake.xlsx")
    assert result == []
    mock_file.assert_called()
