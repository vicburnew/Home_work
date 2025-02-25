import pytest

from src.widget import mask_account_card, get_date


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


# Отрицательное тестирование на несоответствие типа ввода
@pytest.mark.parametrize(
    "card_num",
    [
        (567),
        (),
        (7.02),
    ],
)
def test_mask_account_card_negative_wrong_type_0(card_num):
    """Отрицательное тестирование с использованием параметрирования на вызов исключения TypeError"""
    with pytest.raises(TypeError):
        mask_account_card(card_num)


@pytest.mark.parametrize(
    "card_num",
    [
        ("567"),
        ("123253346364645645645664"),
        ("bdasd 1111222233334444"),
        ("Maestro 15968378687051991"),
        ("Visa 700079228960636"),
        ("Счет 736541084301358743"),
        ("Счет "),
    ],
)
def test_mask_account_card_negative_wrong_type_1(card_num):
    """Отрицательное тестирование с использованием параметрирования на вызов исключения ValueError"""
    with pytest.raises(ValueError):
        mask_account_card(card_num)


@pytest.mark.parametrize("card_num", [("")])
def test_mask_account_card_negative_wrong_type_2(card_num):
    """Отрицательное тестирование с использованием параметрирования на вызов исключения IndexError"""
    with pytest.raises(IndexError):
        mask_account_card(card_num)


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


@pytest.mark.parametrize(
    "date",
    [
        ("11"),
        ("2024"),
        ("03-"),
        (""),
        ("18:35:29.512364"),
        ("2025-07-03"),
        ("2019/07/03T18:35:29"),
        ("03-07-2019T18:35:29)"),
        ("2021-03-11t02:26:18.671407"),
        ("2021-03-11T02.26:18.671407"),
        ("2021-03-11T02:26.18.671407"),
        ("2021-03-11T02:26:18:671407"),
    ],
)
def test_get_date_negative_wrong_type_1(date):
    """Отрицательное тестирование с использованием параметрирования на вызов исключения ValueError"""
    with pytest.raises(ValueError):
        get_date(date)
