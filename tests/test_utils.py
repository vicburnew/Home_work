from unittest.mock import mock_open, patch

from src.utils import read_json_file


def test_read_json_file_1(json_list_initial):
    """Положительный тест на чтение существующего файла"""
    assert read_json_file("./data/") == json_list_initial


def test_read_json_file_2():
    """Отрицательный тест на чтение файла с ошибочным путем"""
    assert read_json_file("../ata/") == []


@patch("builtins.open", new_callable=mock_open, read_data='{"1":{5}}')
def test_read_json_file_3(mock_file):
    """Отрицательный тест на чтение испорченного json-файла"""
    result = read_json_file("../data/")
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_json_file_4(mock_file):
    """Отрицательный тест на чтение пустого json-файла"""
    result = read_json_file("../data/")
    assert result == []
