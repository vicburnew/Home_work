import pytest

from src.widget import mask_account_card


# Тестирование функции mask_account_card

@pytest.mark.parametrize(
    "card_num, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ],
)
def test_mask_account_card_positive(card_num, expected):
    """Положительное тестирование с использованием параметрирования"""
    assert mask_account_card(card_num) == expected

