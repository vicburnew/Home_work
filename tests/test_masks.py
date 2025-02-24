###### Тестирование функции get_mask_card_number #######

import pytest
from src.masks import get_mask_card_number

@pytest.mark.parametrize("card_num, expected", [
    (7000792289606361, "7000 79** **** 6361"),
    (7000723442342523, "7000 72** **** 2523"),
    (7234524442342523, "7234 52** **** 2523")
])
def test_get_mask_card_number_positive(card_num, expected):
    """Положительное тестирование с использованием параметрирования"""
    assert get_mask_card_number(card_num) == expected

## Отрицательное тестирование на несоответствие типа
@pytest.mark.parametrize("card_num", [
    ("7000792289606361"),
    (),
    (7.02)
])
def test_get_mask_card_number_negative_wrong_type_0(card_num):
    """Отрицательное тестирование с использованием параметрирования на вызов исключения TypeError"""
    with pytest.raises(TypeError):
        get_mask_card_number(card_num)

## Отрицательное тестирование на несоответствие длины
@pytest.mark.parametrize("card_num", [
    (11112222333344445),
    (111122223333),
    (1)
])
def test_get_mask_card_number_negative_incorrect_len_0(card_num):
    """Отрицательное тестирование с использованием параметрирования на вызов исключения ValueError"""
    with pytest.raises(ValueError):
        get_mask_card_number(card_num)


##### Тестирование функции get_mask_account ######
