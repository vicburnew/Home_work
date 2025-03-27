import pytest

from src.widget import get_date, mask_account_card

# Тестирование функции mask_account_card


@pytest.mark.parametrize(
    "card_num, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        (" Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        (" Visa 7000792289606361", "Visa 7000 79** **** 6361"),
        ("Mir 7000792289606361", "Mir 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ],
)
def test_mask_account_card_positive(card_num, expected):
    """Положительное тестирование с использованием параметрирования"""
    assert mask_account_card(card_num) == expected



# Тестирование функции get_date


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2021-03-11T02:26:18.671407", "11.03.2021"),
        (" 2024-03-11T02:26:18.671407", "11.03.2024"),
        (" 2025-06-13T02:26:18.671407", "13.06.2025"),
    ],
)
def test_get_date_positive(date, expected):
    """Положительное тестирование с использованием параметрирования"""
    assert get_date(date) == expected


# Отрицательное тестирование на несоответствие типа ввода
@pytest.mark.parametrize(
    "date",
    [
        (11032024),
        (),
        (11.03),
    ],
)
def test_get_date_negative_wrong_type_0(date):
    """Отрицательное тестирование с использованием параметрирования на вызов исключения TypeError"""
    with pytest.raises(TypeError):
        get_date(date)


