import builtins

import pytest
from unittest.mock import patch
from src.interfaces import user_welcome_input



@pytest.mark.parametrize("mock_in, output",[("1",1), ("2",2), ("3",3)])
def test_user_welcome_input_1(mock_in, output):
    """Положительные тесты функции на различные типы ввода """
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

