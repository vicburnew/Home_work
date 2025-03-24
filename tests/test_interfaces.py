import builtins

import pytest
from unittest.mock import patch
from src.interfaces import user_welcome_input, user_status_input, user_input_fbd, user_input_sbda


@pytest.mark.parametrize("mock_in, output",[("1",1), ("2",2), ("3",3)])
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
                        [("EXECUTED","executed"),
                        ("Executed","executed"),
                        ("CANCELED","canceled"),
                        ("canceled", "canceled"),
                        ("Canceled","canceled"),
                        ("pending","pending"),
                        ("Pending","pending"),
                        ("PENDING","pending")
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
                        ("",False)
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
                        ("",False)
                         ])
def test_user_input_sbda(mock_in, output):
    """Тесты функции на различные типы ввода """
    mock_input_data = mock_in
    with patch("builtins.input", read_data=mock_input_data):
        builtins.input.return_value = mock_input_data
        result = user_input_sbda()
        assert result == output

