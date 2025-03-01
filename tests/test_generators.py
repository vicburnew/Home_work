import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# from tests.conftest import transactions


# Тестирование функции test_filter_by_currency


def test_filter_by_currency_USD_1(transactions, transactions_USD_1):
    """Положительный тест на проверку фильтрации по USD"""
    a = filter_by_currency(transactions, "USD")
    assert next(a) == transactions_USD_1


def test_filter_by_currency_USD_2(transactions, transactions_USD_1, transactions_USD_2):
    """Положительный тест на проверку фильтрации по USD"""
    a = filter_by_currency(transactions, "USD")
    assert next(a) == transactions_USD_1
    assert next(a) == transactions_USD_2


def test_filter_by_currency_RUB_1(transactions, transactions_RUB_1):
    """Положительный тест на проверку фильтрации по рублям"""
    a = filter_by_currency(transactions, "RUB")
    assert next(a) == transactions_RUB_1


@pytest.mark.parametrize("empty_list", [{}])
def test_filter_by_currency_3(empty_list):
    """Отрицательный тест - пустой список на входе"""
    with pytest.raises(TypeError):
        a = filter_by_currency(empty_list, "EUR")
        next(a)


def test_filter_by_currency_4(transactions_no_curr):
    """Отрицательный тест на проверку отсутствие транзакций в заданной валюте
    или списка без соответствующих валютных операций"""
    with pytest.raises(TypeError):
        a = filter_by_currency(transactions_no_curr, "USD")
        next(a)


def test_filter_by_currency_StopIteraction(transactions, transactions_USD_1, transactions_USD_2, transactions_USD_3):
    """Отрицательный тест на проверку исключения StopIteraction"""
    a = filter_by_currency(transactions, "USD")
    try:
        assert next(a) == transactions_USD_1
        assert next(a) == transactions_USD_2
        assert next(a) == transactions_USD_3
        assert next(a) == transactions_USD_1
    except StopIteration:
        print("No more transactions")


# Тестирование функции transaction_descriptions


def test_transaction_descriptions(transactions, descriptions):
    """Положительный тест на возврат корректных описаний для каждой транзакции"""
    a = transaction_descriptions(transactions)
    assert list(next(a)) == descriptions


def test_transaction_descriptions_2():
    """Отрицательный тест на пустой список"""
    a = transaction_descriptions([])
    with pytest.raises(TypeError):
        list(next(a))


# Тестирование функции card_number_generator


def test_card_number_generator():
    """Положительный тест №1"""
    a = card_number_generator(1, 3)
    assert next(a) == "0000 0000 0000 0001"
    assert next(a) == "0000 0000 0000 0002"
    assert next(a) == "0000 0000 0000 0003"


def test_card_number_generator_2():
    """Положительный тест №2"""
    a = card_number_generator(99999997, 99999999)
    assert next(a) == "0000 0000 9999 9997"
    assert next(a) == "0000 0000 9999 9998"
    assert next(a) == "0000 0000 9999 9999"


def test_card_number_generator_3():
    """Положительный тест №3"""
    a = card_number_generator(999999999997, 999999999999)
    assert next(a) == "0000 9999 9999 9997"
    assert next(a) == "0000 9999 9999 9998"
    assert next(a) == "0000 9999 9999 9999"


def test_card_number_generator_4():
    """Положительный тест №4"""
    a = card_number_generator(9999999999999997, 9999999999999999)
    assert next(a) == "9999 9999 9999 9997"
    assert next(a) == "9999 9999 9999 9998"
    assert next(a) == "9999 9999 9999 9999"


def test_card_number_generator_5():
    """Отрицательный тест №1"""
    with pytest.raises(TypeError):
        a = card_number_generator(0, 0)
        print(next(a))


def test_card_number_generator_6():
    """Отрицательный тест №2"""
    with pytest.raises(TypeError):
        a = card_number_generator(-1, 1)
        print(next(a))


def test_card_number_generator_7():
    """Отрицательный тест №3"""
    with pytest.raises(TypeError):
        a = card_number_generator(1, 99999999999999999)
        print(next(a))
