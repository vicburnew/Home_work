import builtins

import pytest
from unittest.mock import patch

from src.interfaces import user_welcome_input, user_status_input, user_input_fbd, user_input_sbda, user_input_rf, \
    user_input_sw, filter_by_description, count_operations_by_type


@pytest.mark.parametrize("mock_in, output", [("1", 1), ("2", 2), ("3", 3)])
def test_user_welcome_input_1(mock_in, output):
    """Тесты функции на различные типы ввода """
    mock_input_data = mock_in
    with patch("builtins.input", read_data=mock_input_data):
        builtins.input.return_value = mock_input_data
        result = user_welcome_input()
        assert result == output


# @pytest.mark.parametrize("mock_in, output",[("0",""), ("2",2), ("3",3)])
# def test_user_welcome_input_2():
#     """Отрицательный тест функции на ввод неправильного номера """
#     mock_input_data = "a"
#     with pytest.raises(UnboundLocalError):
#         with patch("builtins.input", read_data=mock_input_data):
#             builtins.input.return_value = mock_input_data
#             user_welcome_input()
#     # assert result == "Введен неправильный номер, повторите ввод! \n\n"

@pytest.mark.parametrize("mock_in, output",
                         [("EXECUTED", "executed"),
                          ("Executed", "executed"),
                          ("CANCELED", "canceled"),
                          ("canceled", "canceled"),
                          ("Canceled", "canceled"),
                          ("pending", "pending"),
                          ("Pending", "pending"),
                          ("PENDING", "pending")
                          ])
def test_user_status_input_1(mock_in, output):
    """Тесты функции на различные типы ввода """
    mock_input_data = mock_in
    with patch("builtins.input", read_data=mock_input_data):
        builtins.input.return_value = mock_input_data
        result = user_status_input()
        assert result == output


@pytest.mark.parametrize("mock_in, output",
                         [("да", True),
                          ("Да", True),
                          ("ДА", True),
                          ("нет", False),
                          ("НЕТ", False),
                          ("asdad", False),
                          ("ывац", False),
                          ("12344", False),
                          ("", False)
                          ])
def test_user_input_fbd(mock_in, output):
    """Тесты функции на различные типы ввода """
    mock_input_data = mock_in
    with patch("builtins.input", read_data=mock_input_data):
        builtins.input.return_value = mock_input_data
        result = user_input_fbd()
        assert result == output


@pytest.mark.parametrize("mock_in, output",
                         [("по возрастанию", True),
                          ("По возрастанию", True),
                          ("по убыванию", False),
                          ("ДА", False),
                          ("нет", False),
                          ("НЕТ", False),
                          ("asdad", False),
                          ("ывац", False),
                          ("12344", False),
                          ("", False)
                          ])
def test_user_input_sbda(mock_in, output):
    """Тесты функции на различные типы ввода """
    mock_input_data = mock_in
    with patch("builtins.input", read_data=mock_input_data):
        builtins.input.return_value = mock_input_data
        result = user_input_sbda()
        assert result == output


@pytest.mark.parametrize("mock_in, output",
                         [("да", True),
                          ("Да", True),
                          ("ДА", True),
                          ("нет", False),
                          ("НЕТ", False),
                          ("asdad", False),
                          ("ывац", False),
                          ("12344", False),
                          ("", False)
                          ])
def test_user_input_rf(mock_in, output):
    """Тесты функции на различные типы ввода """
    mock_input_data = mock_in
    with patch("builtins.input", read_data=mock_input_data):
        builtins.input.return_value = mock_input_data
        result = user_input_rf()
        assert result == output


@pytest.mark.parametrize("mock_in, output",
                         [("да", True),
                          ("Да", True),
                          ("ДА", True),
                          ("нет", False),
                          ("НЕТ", False),
                          ("asdad", False),
                          ("ывац", False),
                          ("12344", False),
                          ("", False)
                          ])
def test_user_input_sw(mock_in, output):
    """Тесты функции на различные типы ввода """
    mock_input_data = mock_in
    with patch("builtins.input", read_data=mock_input_data):
        builtins.input.return_value = mock_input_data
        result = user_input_sw()
        assert result == output


def test_filter_by_description_1(filter_by_description_list_initial, filter_by_description_list_final):
    """Тесты функции на различные типы ввода"""
    assert filter_by_description(filter_by_description_list_initial, "перевод") == filter_by_description_list_final


def test_filter_by_description_2(filter_by_description_list_initial, filter_by_description_list_final):
    """Тесты функции на различные типы ввода"""
    assert filter_by_description(filter_by_description_list_initial, "") == filter_by_description_list_initial


def test_filter_by_description_3(filter_by_description_list_initial, filter_by_description_list_final):
    """Тесты функции на различные типы ввода"""
    assert filter_by_description(filter_by_description_list_initial, " ") == filter_by_description_list_initial


def test_filter_by_description_4(filter_by_description_list_initial, filter_by_description_list_final):
    """Тесты функции на различные типы ввода"""
    assert filter_by_description(filter_by_description_list_initial, "aAS") == filter_by_description_list_initial


def test_filter_by_description_5(filter_by_description_list_initial, filter_by_description_list_final):
    """Тесты функции на различные типы ввода"""
    assert filter_by_description(filter_by_description_list_initial, "ПЕРЕВОД") == filter_by_description_list_final


def test_count_operations_by_type_1(filter_by_description_list_final, list_of_types_fixt, list_of_types_return_fixt):
    """Тестирование функции с различными параметрами """
    assert count_operations_by_type(filter_by_description_list_final, list_of_types_fixt) == list_of_types_return_fixt


def test_count_operations_by_type_2(filter_by_description_list_final):
    """Тестирование функции с различными параметрами """
    assert count_operations_by_type(
        filter_by_description_list_final,
        ["Перевод организации"]) == {"Перевод организации":1}

def test_count_operations_by_type_3(filter_by_description_list_final):
    """Тестирование функции с различными параметрами """
    assert count_operations_by_type(
        filter_by_description_list_final,
        ["Перевод организации", "Перевод с карты на карту"]) == {"Перевод организации":1, "Перевод с карты на карту":3}

