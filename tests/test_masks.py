#Тестирование функции get_mask_card_number
import pytest
from src.masks import get_mask_card_number

@pytest.mark.parametrize("card_num, expected", [
    (7000792289606361, "7000 79** **** 6361"),
    (7000723442342523, "7000 72** **** 2523"),
    (7234524442342523, "7234 52** **** 2523")
])
def test_get_mask_card_number_positive(card_num, expected):
    """Положительное тестирование"""
    assert get_mask_card_number(card_num) == expected



