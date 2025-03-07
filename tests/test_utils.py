from src.utils import read_json_file


def test_read_json_file_1(json_list_initial):
    """Положительный тест на чтение существующего файла"""
    assert read_json_file("../data/") == json_list_initial

