import pytest

from src.masks import get_mask_account, get_mask_card_number

# Тестирование функции get_mask_card_number #######

@pytest.mark.parametrize(
    "card_num, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (7000723442342523, "7000 72** **** 2523"),
        (7234524442342523, "7234 52** **** 2523"),
    ],
)
def test_get_mask_card_number_positive(card_num, expected):
    """Положительное тестирование с использованием параметрирования"""
    assert get_mask_card_number(card_num) == expected


# Отрицательное тестирование на несоответствие типа номера карты
@pytest.mark.parametrize("card_num", [("7000792289606361"), (), (7.02)])
def test_get_mask_card_number_negative_wrong_type_0(card_num):
    """Отрицательное тестирование с использованием параметрирования на вызов исключения TypeError"""
    with pytest.raises(TypeError):
        get_mask_card_number(card_num)


# Отрицательное тестирование на несоответствие длины номера карты
@pytest.mark.parametrize("card_num", [(11112222333344445), (111122223333), (1)])
def test_get_mask_card_number_negative_incorrect_len_0(card_num):
    """Отрицательное тестирование с использованием параметрирования на вызов исключения ValueError"""
    with pytest.raises(ValueError):
        get_mask_card_number(card_num)


# Тестирование функции get_mask_account ######


@pytest.mark.parametrize(
    "acc_num, expected",
    [(73654108430135874305, "**4305"), (70007234423487651122, "**1122"), (72345244423425234563, "**4563")],
)
def test_get_mask_account_positive(acc_num, expected):
    """Положительное тестирование с использованием параметрирования"""
    assert get_mask_account(acc_num) == expected


# Отрицательное тестирование на несоответствие типа номера счета
@pytest.mark.parametrize("acc_num", [("7000792289606361"), (), (7.02)])
def test_get_mask_account_negative_wrong_type_0(acc_num):
    """Отрицательное тестирование с использованием параметрирования на вызов исключения TypeError"""
    with pytest.raises(TypeError):
        get_mask_account(acc_num)


# Отрицательное тестирование на несоответствие длины номера счета
@pytest.mark.parametrize("acc_num", [(111122223333444455551), (111122223333), (1)])
def test_get_mask_account_negative_incorrect_len_0(acc_num):
    """Отрицательное тестирование с использованием параметрирования на вызов исключения ValueError"""
    with pytest.raises(ValueError):
        get_mask_account(acc_num)
